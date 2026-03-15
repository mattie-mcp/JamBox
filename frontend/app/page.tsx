"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import {
  checkHealth,
  fetchMappings,
  fetchTags,
  fetchUnassignedTags,
  createMapping,
  createTag,
  deleteMapping,
  deleteTag,
  searchTracks,
  startDiscovery,
  getDiscoveryStatus,
  stopDiscovery,
  TagMapping,
  Tag,
  SpotifyTrack,
} from "@/lib/api";

function MusicNote({ className, style }: { className?: string; style?: React.CSSProperties }) {
  return (
    <svg
      viewBox="0 0 24 24"
      fill="currentColor"
      className={className}
      style={style}
    >
      <path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55C7.79 13 6 14.79 6 17s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z" />
    </svg>
  );
}

function NfcIcon({ className, style }: { className?: string; style?: React.CSSProperties }) {
  return (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className} style={style}>
      <path d="M6 8.32a7.43 7.43 0 0 1 0 7.36" />
      <path d="M9.46 6.21a11.76 11.76 0 0 1 0 11.58" />
      <path d="M12.91 4.1a15.91 15.91 0 0 1 .01 15.8" />
      <path d="M16.37 2a20.16 20.16 0 0 1 0 20" />
    </svg>
  );
}

function TrashIcon({ className, style }: { className?: string; style?: React.CSSProperties }) {
  return (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className} style={style}>
      <path d="M3 6h18" />
      <path d="M19 6v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6" />
      <path d="M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2" />
    </svg>
  );
}

function SearchIcon({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" className={className}>
      <circle cx="11" cy="11" r="8" />
      <path d="m21 21-4.35-4.35" />
    </svg>
  );
}

function TagIcon({ className, style }: { className?: string; style?: React.CSSProperties }) {
  return (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className} style={style}>
      <path d="M12 2H2v10l9.29 9.29c.94.94 2.48.94 3.42 0l6.58-6.58c.94-.94.94-2.48 0-3.42L12 2Z" />
      <path d="M7 7h.01" />
    </svg>
  );
}

const COLORS = [
  { bg: "bg-[#FF6B6B]/10", border: "border-[#FF6B6B]/30", accent: "#FF6B6B" },
  { bg: "bg-[#4ECDC4]/10", border: "border-[#4ECDC4]/30", accent: "#4ECDC4" },
  { bg: "bg-[#FFB347]/10", border: "border-[#FFB347]/30", accent: "#FFB347" },
  { bg: "bg-[#957FEF]/10", border: "border-[#957FEF]/30", accent: "#957FEF" },
  { bg: "bg-[#74B9FF]/10", border: "border-[#74B9FF]/30", accent: "#74B9FF" },
];

export default function Home() {
  const [mappings, setMappings] = useState<TagMapping[]>([]);
  const [tags, setTags] = useState<Tag[]>([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

  // Add Song form state
  const [showAddSong, setShowAddSong] = useState(false);
  const [unassignedTags, setUnassignedTags] = useState<Tag[]>([]);
  const [selectedTagId, setSelectedTagId] = useState("");
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState<SpotifyTrack[]>([]);
  const [selectedTrack, setSelectedTrack] = useState<SpotifyTrack | null>(null);
  const [isSearching, setIsSearching] = useState(false);

  // Add Tag form state
  const [showAddTag, setShowAddTag] = useState(false);
  const [discoveryActive, setDiscoveryActive] = useState(false);
  const [discoveredTagId, setDiscoveredTagId] = useState<string | null>(null);
  const [secondsRemaining, setSecondsRemaining] = useState<number | null>(null);
  const [friendlyName, setFriendlyName] = useState("");
  const pollRef = useRef<ReturnType<typeof setInterval> | null>(null);

  // Connection status
  const [connected, setConnected] = useState<boolean | null>(null);

  useEffect(() => {
    let cancelled = false;
    async function ping() {
      const ok = await checkHealth();
      if (!cancelled) setConnected(ok);
    }
    ping();
    const interval = setInterval(ping, 10000);
    return () => { cancelled = true; clearInterval(interval); };
  }, []);

  const loadData = useCallback(async () => {
    try {
      const [mappingsData, tagsData] = await Promise.all([
        fetchMappings(),
        fetchTags(),
      ]);
      setMappings(mappingsData);
      setTags(tagsData);
    } catch {
      setError("Could not load data. Is the backend running?");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    loadData();
  }, [loadData]);

  // Helper to find tag friendly name by tag_id
  function getTagName(tagId: string): string | undefined {
    return tags.find((t) => t.tag_id === tagId)?.friendly_name;
  }

  // --- Add Song ---

  async function openAddSong() {
    setShowAddSong(true);
    try {
      const available = await fetchUnassignedTags();
      setUnassignedTags(available);
    } catch {
      setError("Could not load available tags.");
    }
  }

  function resetAddSong() {
    setShowAddSong(false);
    setSelectedTagId("");
    setSelectedTrack(null);
    setSearchResults([]);
    setSearchQuery("");
    setUnassignedTags([]);
  }

  async function handleSearch() {
    if (!searchQuery.trim()) return;
    setIsSearching(true);
    try {
      const results = await searchTracks(searchQuery);
      setSearchResults(results);
    } catch {
      setError("Search failed. Check Spotify authentication.");
    } finally {
      setIsSearching(false);
    }
  }

  async function handleCreateMapping() {
    if (!selectedTagId || !selectedTrack) return;
    try {
      await createMapping({
        tag_id: selectedTagId,
        spotify_uri: selectedTrack.uri,
        name: `${selectedTrack.name} - ${selectedTrack.artist}`,
      });
      resetAddSong();
      loadData();
    } catch {
      setError("Failed to create mapping. Tag may already be assigned.");
    }
  }

  async function handleDelete(id: number) {
    try {
      await deleteMapping(id);
      loadData();
    } catch {
      setError("Failed to delete mapping.");
    }
  }

  async function handleDeleteTag(tagId: string) {
    try {
      await deleteTag(tagId);
      loadData();
    } catch {
      setError("Failed to delete tag.");
    }
  }

  // --- Add Tag (Discovery) ---

  function stopPolling() {
    if (pollRef.current) {
      clearInterval(pollRef.current);
      pollRef.current = null;
    }
  }

  async function openAddTag() {
    setShowAddTag(true);
    setDiscoveredTagId(null);
    setFriendlyName("");
    setDiscoveryActive(true);
    try {
      await startDiscovery();
      pollRef.current = setInterval(async () => {
        try {
          const status = await getDiscoveryStatus();
          if (status.detected_tag_id) {
            setDiscoveredTagId(status.detected_tag_id);
            setDiscoveryActive(false);
            setSecondsRemaining(null);
            stopPolling();
          } else if (!status.active) {
            setDiscoveryActive(false);
            setSecondsRemaining(null);
            stopPolling();
          } else {
            setSecondsRemaining(status.seconds_remaining);
          }
        } catch {
          stopPolling();
          setDiscoveryActive(false);
        }
      }, 1000);
    } catch {
      setError("Failed to start NFC discovery.");
      setDiscoveryActive(false);
    }
  }

  function resetAddTag() {
    stopPolling();
    if (discoveryActive) {
      stopDiscovery().catch(() => {});
    }
    setShowAddTag(false);
    setDiscoveryActive(false);
    setDiscoveredTagId(null);
    setFriendlyName("");
    setSecondsRemaining(null);
  }

  async function retryDiscovery() {
    setDiscoveredTagId(null);
    setDiscoveryActive(true);
    try {
      await startDiscovery();
      pollRef.current = setInterval(async () => {
        try {
          const status = await getDiscoveryStatus();
          if (status.detected_tag_id) {
            setDiscoveredTagId(status.detected_tag_id);
            setDiscoveryActive(false);
            setSecondsRemaining(null);
            stopPolling();
          } else if (!status.active) {
            setDiscoveryActive(false);
            setSecondsRemaining(null);
            stopPolling();
          } else {
            setSecondsRemaining(status.seconds_remaining);
          }
        } catch {
          stopPolling();
          setDiscoveryActive(false);
        }
      }, 1000);
    } catch {
      setError("Failed to start NFC discovery.");
      setDiscoveryActive(false);
    }
  }

  async function handleRegisterTag() {
    if (!discoveredTagId || !friendlyName.trim()) return;
    try {
      await createTag({
        tag_id: discoveredTagId,
        friendly_name: friendlyName.trim(),
      });
      resetAddTag();
      loadData();
    } catch {
      setError("Failed to register tag. It may already be registered.");
    }
  }

  // Clean up polling on unmount
  useEffect(() => {
    return () => stopPolling();
  }, []);

  return (
    <main className="relative z-10 min-h-screen px-4 py-8 max-w-xl mx-auto">
      {/* Header */}
      <header className="text-center mb-10 animate-bounce-in">
        <div className="inline-flex items-center gap-3 mb-2">
          <div className="relative">
            <div
              className="w-14 h-14 rounded-2xl flex items-center justify-center shadow-lg"
              style={{
                background: "linear-gradient(135deg, #FF6B6B, #FFB347)",
              }}
            >
              <MusicNote className="w-7 h-7 text-white" />
            </div>
            <div
              className="absolute -top-1 -right-1 w-5 h-5 rounded-full flex items-center justify-center text-[8px] font-bold text-white shadow-md"
              style={{ background: "#4ECDC4" }}
            >
              J
            </div>
          </div>
          <div>
            <h1
              className="text-4xl font-extrabold tracking-tight"
              style={{
                fontFamily: "'Baloo 2', cursive",
                background: "linear-gradient(135deg, #FF6B6B, #FFB347)",
                WebkitBackgroundClip: "text",
                WebkitTextFillColor: "transparent",
              }}
            >
              JamBox
            </h1>
          </div>
        </div>
        <p
          className="text-sm font-medium"
          style={{ color: "var(--warm-gray)" }}
        >
          Jamie&apos;s magic music toybox
        </p>
        {connected !== null && (
          <div className="inline-flex items-center gap-1.5 mt-2 px-3 py-1 rounded-full text-xs font-medium"
            style={{
              background: connected ? "rgba(78, 205, 196, 0.1)" : "rgba(255, 118, 117, 0.1)",
              color: connected ? "#3DB8B0" : "#D63031",
            }}
          >
            <span
              className="w-2 h-2 rounded-full inline-block"
              style={{
                background: connected ? "#4ECDC4" : "#FF7675",
                boxShadow: connected ? "0 0 6px rgba(78, 205, 196, 0.5)" : "none",
              }}
            />
            {connected ? "Connected to Pi" : "Pi unreachable"}
          </div>
        )}
      </header>

      {/* Error Banner */}
      {error && (
        <div
          className="animate-slide-up mb-6 p-4 rounded-2xl border-2 flex items-center justify-between"
          style={{
            background: "rgba(255, 118, 117, 0.08)",
            borderColor: "rgba(255, 118, 117, 0.3)",
          }}
        >
          <span className="text-sm font-medium" style={{ color: "#D63031" }}>
            {error}
          </span>
          <button
            onClick={() => setError("")}
            className="ml-3 text-xs font-bold px-3 py-1 rounded-full transition-all hover:scale-105"
            style={{
              background: "rgba(214, 48, 49, 0.1)",
              color: "#D63031",
            }}
          >
            OK
          </button>
        </div>
      )}

      {/* Action Buttons */}
      {!showAddSong && !showAddTag && (
        <div className="flex gap-3 mb-6">
          <button
            onClick={openAddTag}
            className="flex-1 flex items-center justify-center gap-2 px-4 py-2.5 rounded-full font-bold text-sm text-white shadow-md transition-all hover:scale-105 hover:shadow-lg active:scale-95"
            style={{
              fontFamily: "'Baloo 2', cursive",
              background: "linear-gradient(135deg, #957FEF, #7B68D4)",
            }}
          >
            <NfcIcon className="w-4 h-4" /> Add New Tag
          </button>
          <button
            onClick={openAddSong}
            className="flex-1 flex items-center justify-center gap-2 px-4 py-2.5 rounded-full font-bold text-sm text-white shadow-md transition-all hover:scale-105 hover:shadow-lg active:scale-95"
            style={{
              fontFamily: "'Baloo 2', cursive",
              background: "linear-gradient(135deg, #4ECDC4, #3DB8B0)",
            }}
          >
            <span className="text-lg leading-none">+</span> Add Song
          </button>
        </div>
      )}

      {/* Add New Tag Form (Discovery) */}
      {showAddTag && (
        <section
          className="animate-slide-up rounded-3xl border-2 p-6 shadow-lg mb-8"
          style={{
            background: "var(--card-bg)",
            borderColor: "var(--light-gray)",
          }}
        >
          <div className="flex items-center justify-between mb-5">
            <h2
              className="text-xl font-bold"
              style={{ fontFamily: "'Baloo 2', cursive" }}
            >
              Register New Tag
            </h2>
            <button
              onClick={resetAddTag}
              className="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold transition-all hover:scale-110 active:scale-90"
              style={{
                background: "var(--light-gray)",
                color: "var(--warm-gray)",
              }}
            >
              x
            </button>
          </div>

          {discoveryActive && (
            <div className="text-center py-8">
              <div className="inline-flex items-center justify-center w-20 h-20 rounded-3xl mb-4 animate-pulse" style={{ background: "rgba(149, 127, 239, 0.12)" }}>
                <NfcIcon className="w-10 h-10" style={{ color: "#957FEF" }} />
              </div>
              <p className="font-bold text-lg mb-1" style={{ fontFamily: "'Baloo 2', cursive" }}>
                Place tag on reader...
              </p>
              <p className="text-sm" style={{ color: "var(--warm-gray)" }}>
                {secondsRemaining !== null
                  ? `Listening... ${secondsRemaining}s remaining`
                  : "Starting discovery..."}
              </p>
            </div>
          )}

          {!discoveryActive && !discoveredTagId && (
            <div className="text-center py-8">
              <p className="font-bold text-lg mb-2" style={{ fontFamily: "'Baloo 2', cursive" }}>
                No tag detected
              </p>
              <p className="text-sm mb-5" style={{ color: "var(--warm-gray)" }}>
                The scan timed out. Make sure the tag is placed on the reader.
              </p>
              <button
                onClick={retryDiscovery}
                className="px-6 py-3 rounded-full font-bold text-white shadow-lg transition-all hover:scale-105 active:scale-95"
                style={{
                  fontFamily: "'Baloo 2', cursive",
                  background: "linear-gradient(135deg, #957FEF, #7B68D4)",
                }}
              >
                Try Again
              </button>
            </div>
          )}

          {discoveredTagId && (
            <div>
              <div
                className="animate-slide-up mb-5 flex items-center gap-3 p-3 rounded-2xl border-2"
                style={{
                  background: "rgba(149, 127, 239, 0.06)",
                  borderColor: "rgba(149, 127, 239, 0.3)",
                }}
              >
                <div
                  className="w-10 h-10 rounded-xl flex items-center justify-center shrink-0"
                  style={{ background: "#957FEF" }}
                >
                  <NfcIcon className="w-5 h-5 text-white" />
                </div>
                <div>
                  <p className="text-xs font-bold uppercase tracking-wider" style={{ color: "#957FEF" }}>
                    Tag Detected
                  </p>
                  <p className="text-sm font-mono" style={{ color: "var(--charcoal)" }}>
                    {discoveredTagId}
                  </p>
                </div>
              </div>

              <div className="mb-5">
                <label
                  className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider mb-2"
                  style={{ color: "var(--warm-gray)" }}
                >
                  <TagIcon className="w-3.5 h-3.5" />
                  Friendly Name
                </label>
                <input
                  type="text"
                  value={friendlyName}
                  onChange={(e) => setFriendlyName(e.target.value)}
                  placeholder="e.g. Blue Dinosaur"
                  className="w-full px-4 py-3 rounded-xl border-2 text-sm transition-all focus:outline-none focus:scale-[1.01]"
                  style={{
                    borderColor: friendlyName ? "#957FEF" : "var(--light-gray)",
                    background: friendlyName ? "rgba(149, 127, 239, 0.04)" : "transparent",
                  }}
                  autoFocus
                />
              </div>

              <button
                onClick={handleRegisterTag}
                disabled={!friendlyName.trim()}
                className="w-full py-3.5 rounded-xl font-bold text-white text-sm shadow-lg transition-all hover:scale-[1.02] hover:shadow-xl active:scale-[0.98] disabled:opacity-30 disabled:hover:scale-100 disabled:shadow-none disabled:cursor-not-allowed"
                style={{
                  fontFamily: "'Baloo 2', cursive",
                  fontSize: "1rem",
                  background: !friendlyName.trim()
                    ? "var(--light-gray)"
                    : "linear-gradient(135deg, #957FEF, #7B68D4)",
                }}
              >
                {friendlyName.trim() ? "Register Tag" : "Enter a name to continue"}
              </button>
            </div>
          )}
        </section>
      )}

      {/* Add Song Form */}
      {showAddSong && (
        <section
          className="animate-slide-up rounded-3xl border-2 p-6 shadow-lg mb-8"
          style={{
            background: "var(--card-bg)",
            borderColor: "var(--light-gray)",
          }}
        >
          <div className="flex items-center justify-between mb-5">
            <h2
              className="text-xl font-bold"
              style={{ fontFamily: "'Baloo 2', cursive" }}
            >
              New Song Mapping
            </h2>
            <button
              onClick={resetAddSong}
              className="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold transition-all hover:scale-110 active:scale-90"
              style={{
                background: "var(--light-gray)",
                color: "var(--warm-gray)",
              }}
            >
              x
            </button>
          </div>

          {/* Step 1: Pick a Tag */}
          <div className="mb-5">
            <label
              className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider mb-2"
              style={{ color: "var(--warm-gray)" }}
            >
              <NfcIcon className="w-3.5 h-3.5" />
              Choose a Tag
            </label>
            {unassignedTags.length === 0 ? (
              <div
                className="p-4 rounded-xl border-2 text-center"
                style={{ borderColor: "var(--light-gray)", borderStyle: "dashed" }}
              >
                <p className="text-sm font-medium mb-2" style={{ color: "var(--warm-gray)" }}>
                  No available tags
                </p>
                <button
                  onClick={() => { resetAddSong(); openAddTag(); }}
                  className="text-sm font-bold px-4 py-1.5 rounded-full transition-all hover:scale-105"
                  style={{ color: "#957FEF", background: "rgba(149, 127, 239, 0.1)" }}
                >
                  Register a tag first
                </button>
              </div>
            ) : (
              <div className="space-y-2">
                {unassignedTags.map((tag) => {
                  const isSelected = selectedTagId === tag.tag_id;
                  return (
                    <button
                      key={tag.tag_id}
                      onClick={() => setSelectedTagId(tag.tag_id)}
                      className="w-full flex items-center gap-3 p-3 rounded-xl border-2 text-left transition-all hover:scale-[1.01]"
                      style={{
                        borderColor: isSelected ? "rgba(78, 205, 196, 0.4)" : "var(--light-gray)",
                        background: isSelected ? "rgba(78, 205, 196, 0.06)" : "transparent",
                      }}
                    >
                      <div
                        className="w-9 h-9 rounded-lg flex items-center justify-center shrink-0"
                        style={{ background: isSelected ? "#4ECDC4" : "var(--light-gray)" }}
                      >
                        <TagIcon className="w-4 h-4" style={{ color: isSelected ? "white" : "var(--warm-gray)" }} />
                      </div>
                      <div className="flex-1 min-w-0">
                        <p className="text-sm font-bold truncate" style={{ fontFamily: "'Baloo 2', cursive" }}>
                          {tag.friendly_name}
                        </p>
                        <p className="text-xs font-mono truncate" style={{ color: "var(--warm-gray)" }}>
                          {tag.tag_id}
                        </p>
                      </div>
                      {isSelected && (
                        <div
                          className="w-6 h-6 rounded-full flex items-center justify-center shrink-0 text-white text-xs font-bold"
                          style={{ background: "#4ECDC4" }}
                        >
                          &#10003;
                        </div>
                      )}
                    </button>
                  );
                })}
              </div>
            )}
          </div>

          {/* Step 2: Search Spotify */}
          <div className="mb-5">
            <label
              className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider mb-2"
              style={{ color: "var(--warm-gray)" }}
            >
              <SearchIcon className="w-3.5 h-3.5" />
              Find a Song
            </label>
            <div className="flex gap-2">
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                onKeyDown={(e) => e.key === "Enter" && handleSearch()}
                placeholder="Search Spotify..."
                className="flex-1 px-4 py-3 rounded-xl border-2 text-sm transition-all focus:outline-none focus:scale-[1.01]"
                style={{ borderColor: "var(--light-gray)" }}
              />
              <button
                onClick={handleSearch}
                disabled={isSearching}
                className="px-5 py-3 rounded-xl font-bold text-sm text-white transition-all hover:scale-105 active:scale-95 disabled:opacity-50"
                style={{
                  fontFamily: "'Baloo 2', cursive",
                  background: "linear-gradient(135deg, #1DB954, #1AA34A)",
                }}
              >
                {isSearching ? "..." : "Search"}
              </button>
            </div>
          </div>

          {/* Search Results */}
          {searchResults.length > 0 && (
            <div className="mb-5 max-h-64 overflow-y-auto rounded-2xl border-2 p-2" style={{ borderColor: "var(--light-gray)" }}>
              <ul className="space-y-1">
                {searchResults.map((track, i) => {
                  const isSelected = selectedTrack?.uri === track.uri;
                  return (
                    <li
                      key={track.uri}
                      onClick={() => setSelectedTrack(track)}
                      className="animate-slide-up flex items-center gap-3 p-2.5 rounded-xl cursor-pointer transition-all hover:scale-[1.01]"
                      style={{
                        animationDelay: `${i * 30}ms`,
                        background: isSelected
                          ? "rgba(78, 205, 196, 0.12)"
                          : "transparent",
                        border: isSelected
                          ? "2px solid rgba(78, 205, 196, 0.4)"
                          : "2px solid transparent",
                      }}
                    >
                      {track.image_url ? (
                        <img
                          src={track.image_url}
                          alt=""
                          className="w-11 h-11 rounded-lg shadow-sm object-cover"
                        />
                      ) : (
                        <div
                          className="w-11 h-11 rounded-lg flex items-center justify-center"
                          style={{ background: "var(--light-gray)" }}
                        >
                          <MusicNote className="w-5 h-5" style={{ color: "var(--warm-gray)" }} />
                        </div>
                      )}
                      <div className="flex-1 min-w-0">
                        <p className="text-sm font-bold truncate">{track.name}</p>
                        <p className="text-xs truncate" style={{ color: "var(--warm-gray)" }}>
                          {track.artist}
                        </p>
                      </div>
                      {isSelected && (
                        <div
                          className="w-6 h-6 rounded-full flex items-center justify-center shrink-0 text-white text-xs font-bold"
                          style={{ background: "#4ECDC4" }}
                        >
                          &#10003;
                        </div>
                      )}
                    </li>
                  );
                })}
              </ul>
            </div>
          )}

          {/* Selected Track Preview */}
          {selectedTrack && (
            <div
              className="animate-slide-up mb-5 flex items-center gap-3 p-3 rounded-2xl border-2"
              style={{
                background: "rgba(78, 205, 196, 0.06)",
                borderColor: "rgba(78, 205, 196, 0.3)",
              }}
            >
              {selectedTrack.image_url && (
                <img
                  src={selectedTrack.image_url}
                  alt=""
                  className="w-12 h-12 rounded-xl shadow-md object-cover"
                />
              )}
              <div className="flex-1 min-w-0">
                <p className="text-xs font-bold uppercase tracking-wider" style={{ color: "#4ECDC4" }}>
                  Selected
                </p>
                <p className="text-sm font-bold truncate">{selectedTrack.name}</p>
                <p className="text-xs truncate" style={{ color: "var(--warm-gray)" }}>
                  {selectedTrack.artist}
                </p>
              </div>
            </div>
          )}

          {/* Save Button */}
          <button
            onClick={handleCreateMapping}
            disabled={!selectedTagId || !selectedTrack}
            className="w-full py-3.5 rounded-xl font-bold text-white text-sm shadow-lg transition-all hover:scale-[1.02] hover:shadow-xl active:scale-[0.98] disabled:opacity-30 disabled:hover:scale-100 disabled:shadow-none disabled:cursor-not-allowed"
            style={{
              fontFamily: "'Baloo 2', cursive",
              fontSize: "1rem",
              background: !selectedTagId || !selectedTrack
                ? "var(--light-gray)"
                : "linear-gradient(135deg, #FF6B6B, #FFB347)",
            }}
          >
            {!selectedTagId
              ? "Pick a tag to continue"
              : !selectedTrack
                ? "Search & pick a song"
                : "Save to JamBox"}
          </button>
        </section>
      )}

      {/* Mappings List */}
      <section className="mb-8">
        <h2
          className="text-lg font-bold mb-4"
          style={{ fontFamily: "'Baloo 2', cursive", color: "var(--charcoal)" }}
        >
          {mappings.length > 0
            ? `${mappings.length} song${mappings.length !== 1 ? "s" : ""} loaded`
            : "No songs yet"}
        </h2>

        {loading ? (
          <div className="flex flex-col items-center py-16 gap-3">
            <div
              className="w-10 h-10 rounded-full border-4 border-t-transparent animate-spin"
              style={{ borderColor: "#4ECDC4", borderTopColor: "transparent" }}
            />
            <p className="text-sm font-medium" style={{ color: "var(--warm-gray)" }}>
              Loading Jamie&apos;s songs...
            </p>
          </div>
        ) : mappings.length === 0 && !showAddSong && !showAddTag ? (
          <div className="text-center py-16">
            <div className="inline-flex items-center justify-center w-20 h-20 rounded-3xl mb-4" style={{ background: "rgba(149, 127, 239, 0.1)" }}>
              <NfcIcon className="w-10 h-10" style={{ color: "#957FEF" }} />
            </div>
            <p className="font-bold text-lg mb-1" style={{ fontFamily: "'Baloo 2', cursive" }}>
              Ready to jam!
            </p>
            <p className="text-sm mb-5" style={{ color: "var(--warm-gray)" }}>
              Register an NFC tag, then pair it with a song
            </p>
            <button
              onClick={openAddTag}
              className="px-6 py-3 rounded-full font-bold text-white shadow-lg transition-all hover:scale-105 hover:shadow-xl active:scale-95"
              style={{
                fontFamily: "'Baloo 2', cursive",
                background: "linear-gradient(135deg, #957FEF, #7B68D4)",
              }}
            >
              Add First Tag
            </button>
          </div>
        ) : (
          <ul className="space-y-3">
            {mappings.map((m, i) => {
              const color = COLORS[i % COLORS.length];
              const tagName = getTagName(m.tag_id);
              return (
                <li
                  key={m.id}
                  className={`animate-slide-up group flex items-center gap-4 p-4 rounded-2xl border-2 transition-all hover:shadow-md ${color.bg} ${color.border}`}
                  style={{ animationDelay: `${i * 60}ms` }}
                >
                  <div
                    className="w-11 h-11 rounded-xl flex items-center justify-center shrink-0 shadow-sm"
                    style={{ background: color.accent }}
                  >
                    <MusicNote className="w-5 h-5 text-white" />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="font-bold text-sm truncate" style={{ fontFamily: "'Baloo 2', cursive" }}>
                      {m.name}
                    </p>
                    <div className="flex items-center gap-1.5 mt-0.5">
                      <TagIcon className="w-3 h-3" style={{ color: "var(--warm-gray)" }} />
                      <p className="text-xs truncate" style={{ color: "var(--warm-gray)" }}>
                        {tagName || m.tag_id}
                      </p>
                    </div>
                  </div>
                  <button
                    onClick={() => handleDelete(m.id)}
                    className="opacity-0 group-hover:opacity-100 p-2 rounded-xl transition-all hover:scale-110 active:scale-90"
                    style={{ background: "rgba(214, 48, 49, 0.1)" }}
                    title="Remove mapping"
                  >
                    <TrashIcon className="w-4 h-4" style={{ color: "#D63031" }} />
                  </button>
                </li>
              );
            })}
          </ul>
        )}
      </section>

      {/* Registered Tags */}
      {tags.length > 0 && (
        <section className="mb-8">
          <h2
            className="text-lg font-bold mb-4"
            style={{ fontFamily: "'Baloo 2', cursive", color: "var(--charcoal)" }}
          >
            {tags.length} tag{tags.length !== 1 ? "s" : ""} registered
          </h2>
          <ul className="space-y-2">
            {tags.map((tag, i) => {
              const color = COLORS[(i + 2) % COLORS.length];
              const hasMapping = mappings.some((m) => m.tag_id === tag.tag_id);
              return (
                <li
                  key={tag.id}
                  className={`animate-slide-up group flex items-center gap-3 p-3 rounded-2xl border-2 ${color.bg} ${color.border}`}
                  style={{ animationDelay: `${i * 60}ms` }}
                >
                  <div
                    className="w-9 h-9 rounded-lg flex items-center justify-center shrink-0"
                    style={{ background: color.accent }}
                  >
                    <TagIcon className="w-4 h-4 text-white" />
                  </div>
                  <div className="flex-1 min-w-0">
                    <p className="text-sm font-bold truncate" style={{ fontFamily: "'Baloo 2', cursive" }}>
                      {tag.friendly_name}
                    </p>
                    <p className="text-xs font-mono truncate" style={{ color: "var(--warm-gray)" }}>
                      {tag.tag_id} {hasMapping ? "" : "  (no song)"}
                    </p>
                  </div>
                  <button
                    onClick={() => handleDeleteTag(tag.tag_id)}
                    className="opacity-0 group-hover:opacity-100 p-2 rounded-xl transition-all hover:scale-110 active:scale-90"
                    style={{ background: "rgba(214, 48, 49, 0.1)" }}
                    title="Remove tag"
                  >
                    <TrashIcon className="w-4 h-4" style={{ color: "#D63031" }} />
                  </button>
                </li>
              );
            })}
          </ul>
        </section>
      )}

      {/* Footer */}
      <footer className="text-center mt-12 pb-6">
        <p className="text-xs" style={{ color: "var(--light-gray)" }}>
          JamBox &mdash; made with love for Jamie
        </p>
      </footer>
    </main>
  );
}
