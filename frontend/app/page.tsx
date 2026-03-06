"use client";

import { useEffect, useState } from "react";
import {
  fetchMappings,
  createMapping,
  deleteMapping,
  searchTracks,
  TagMapping,
  SpotifyTrack,
} from "@/lib/api";

function MusicNote({ className }: { className?: string }) {
  return (
    <svg
      viewBox="0 0 24 24"
      fill="currentColor"
      className={className}
    >
      <path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55C7.79 13 6 14.79 6 17s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z" />
    </svg>
  );
}

function NfcIcon({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}>
      <path d="M6 8.32a7.43 7.43 0 0 1 0 7.36" />
      <path d="M9.46 6.21a11.76 11.76 0 0 1 0 11.58" />
      <path d="M12.91 4.1a15.91 15.91 0 0 1 .01 15.8" />
      <path d="M16.37 2a20.16 20.16 0 0 1 0 20" />
    </svg>
  );
}

function TrashIcon({ className }: { className?: string }) {
  return (
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}>
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

const COLORS = [
  { bg: "bg-[#FF6B6B]/10", border: "border-[#FF6B6B]/30", accent: "#FF6B6B" },
  { bg: "bg-[#4ECDC4]/10", border: "border-[#4ECDC4]/30", accent: "#4ECDC4" },
  { bg: "bg-[#FFB347]/10", border: "border-[#FFB347]/30", accent: "#FFB347" },
  { bg: "bg-[#957FEF]/10", border: "border-[#957FEF]/30", accent: "#957FEF" },
  { bg: "bg-[#74B9FF]/10", border: "border-[#74B9FF]/30", accent: "#74B9FF" },
];

export default function Home() {
  const [mappings, setMappings] = useState<TagMapping[]>([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState<SpotifyTrack[]>([]);
  const [selectedTrack, setSelectedTrack] = useState<SpotifyTrack | null>(null);
  const [tagId, setTagId] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);
  const [showAddForm, setShowAddForm] = useState(false);
  const [isSearching, setIsSearching] = useState(false);

  async function loadMappings() {
    try {
      const data = await fetchMappings();
      setMappings(data);
    } catch {
      setError("Could not load mappings. Is the backend running?");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadMappings();
  }, []);

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

  async function handleCreate() {
    if (!tagId.trim() || !selectedTrack) return;
    try {
      await createMapping({
        tag_id: tagId.trim(),
        spotify_uri: selectedTrack.uri,
        name: `${selectedTrack.name} - ${selectedTrack.artist}`,
      });
      setTagId("");
      setSelectedTrack(null);
      setSearchResults([]);
      setSearchQuery("");
      setShowAddForm(false);
      loadMappings();
    } catch {
      setError("Failed to create mapping. Tag may already be assigned.");
    }
  }

  async function handleDelete(id: number) {
    try {
      await deleteMapping(id);
      loadMappings();
    } catch {
      setError("Failed to delete mapping.");
    }
  }

  function resetForm() {
    setShowAddForm(false);
    setTagId("");
    setSelectedTrack(null);
    setSearchResults([]);
    setSearchQuery("");
  }

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

      {/* Mappings List */}
      <section className="mb-8">
        <div className="flex items-center justify-between mb-4">
          <h2
            className="text-lg font-bold"
            style={{ fontFamily: "'Baloo 2', cursive", color: "var(--charcoal)" }}
          >
            {mappings.length > 0
              ? `${mappings.length} song${mappings.length !== 1 ? "s" : ""} loaded`
              : "No songs yet"}
          </h2>
          {!showAddForm && (
            <button
              onClick={() => setShowAddForm(true)}
              className="flex items-center gap-2 px-4 py-2 rounded-full font-bold text-sm text-white shadow-md transition-all hover:scale-105 hover:shadow-lg active:scale-95"
              style={{
                fontFamily: "'Baloo 2', cursive",
                background: "linear-gradient(135deg, #4ECDC4, #3DB8B0)",
              }}
            >
              <span className="text-lg leading-none">+</span> Add Song
            </button>
          )}
        </div>

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
        ) : mappings.length === 0 && !showAddForm ? (
          <div className="text-center py-16">
            <div className="inline-flex items-center justify-center w-20 h-20 rounded-3xl mb-4" style={{ background: "rgba(149, 127, 239, 0.1)" }}>
              <NfcIcon className="w-10 h-10" style={{ color: "#957FEF" }} />
            </div>
            <p className="font-bold text-lg mb-1" style={{ fontFamily: "'Baloo 2', cursive" }}>
              Ready to jam!
            </p>
            <p className="text-sm mb-5" style={{ color: "var(--warm-gray)" }}>
              Add your first NFC tag + song pairing
            </p>
            <button
              onClick={() => setShowAddForm(true)}
              className="px-6 py-3 rounded-full font-bold text-white shadow-lg transition-all hover:scale-105 hover:shadow-xl active:scale-95"
              style={{
                fontFamily: "'Baloo 2', cursive",
                background: "linear-gradient(135deg, #FF6B6B, #FFB347)",
              }}
            >
              Add First Song
            </button>
          </div>
        ) : (
          <ul className="space-y-3">
            {mappings.map((m, i) => {
              const color = COLORS[i % COLORS.length];
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
                      <NfcIcon className="w-3 h-3" style={{ color: "var(--warm-gray)" }} />
                      <p className="text-xs font-mono truncate" style={{ color: "var(--warm-gray)" }}>
                        {m.tag_id}
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

      {/* Add New Mapping Form */}
      {showAddForm && (
        <section
          className="animate-slide-up rounded-3xl border-2 p-6 shadow-lg"
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
              onClick={resetForm}
              className="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold transition-all hover:scale-110 active:scale-90"
              style={{
                background: "var(--light-gray)",
                color: "var(--warm-gray)",
              }}
            >
              x
            </button>
          </div>

          {/* Step 1: Tag ID */}
          <div className="mb-5">
            <label
              className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider mb-2"
              style={{ color: "var(--warm-gray)" }}
            >
              <NfcIcon className="w-3.5 h-3.5" />
              NFC Tag ID
            </label>
            <input
              type="text"
              value={tagId}
              onChange={(e) => setTagId(e.target.value)}
              placeholder="e.g. 04:A2:3B:5C:6D:7E:80"
              className="w-full px-4 py-3 rounded-xl border-2 text-sm font-mono transition-all focus:outline-none focus:scale-[1.01]"
              style={{
                borderColor: tagId ? "#4ECDC4" : "var(--light-gray)",
                background: tagId ? "rgba(78, 205, 196, 0.04)" : "transparent",
              }}
            />
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
            onClick={handleCreate}
            disabled={!tagId.trim() || !selectedTrack}
            className="w-full py-3.5 rounded-xl font-bold text-white text-sm shadow-lg transition-all hover:scale-[1.02] hover:shadow-xl active:scale-[0.98] disabled:opacity-30 disabled:hover:scale-100 disabled:shadow-none disabled:cursor-not-allowed"
            style={{
              fontFamily: "'Baloo 2', cursive",
              fontSize: "1rem",
              background: !tagId.trim() || !selectedTrack
                ? "var(--light-gray)"
                : "linear-gradient(135deg, #FF6B6B, #FFB347)",
            }}
          >
            {!tagId.trim()
              ? "Enter a tag ID to continue"
              : !selectedTrack
                ? "Search & pick a song"
                : "Save to JamBox"}
          </button>
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
