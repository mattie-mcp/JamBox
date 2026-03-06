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

export default function Home() {
  const [mappings, setMappings] = useState<TagMapping[]>([]);
  const [searchQuery, setSearchQuery] = useState("");
  const [searchResults, setSearchResults] = useState<SpotifyTrack[]>([]);
  const [selectedTrack, setSelectedTrack] = useState<SpotifyTrack | null>(null);
  const [tagId, setTagId] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(true);

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
    try {
      const results = await searchTracks(searchQuery);
      setSearchResults(results);
    } catch {
      setError("Search failed. Check Spotify authentication.");
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

  return (
    <main className="min-h-screen bg-gray-50 p-6 max-w-2xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">JamBox</h1>

      {error && (
        <div className="bg-red-100 border border-red-300 text-red-700 rounded p-3 mb-4">
          {error}
          <button className="ml-2 underline" onClick={() => setError("")}>
            dismiss
          </button>
        </div>
      )}

      {/* Current Mappings */}
      <section className="mb-8">
        <h2 className="text-xl font-semibold mb-3">Tag Mappings</h2>
        {loading ? (
          <p className="text-gray-500">Loading...</p>
        ) : mappings.length === 0 ? (
          <p className="text-gray-500">No mappings yet. Add one below.</p>
        ) : (
          <ul className="space-y-2">
            {mappings.map((m) => (
              <li
                key={m.id}
                className="flex items-center justify-between bg-white rounded-lg shadow p-4"
              >
                <div>
                  <p className="font-medium">{m.name}</p>
                  <p className="text-sm text-gray-500">Tag: {m.tag_id}</p>
                </div>
                <button
                  onClick={() => handleDelete(m.id)}
                  className="text-red-500 hover:text-red-700 text-sm"
                >
                  Remove
                </button>
              </li>
            ))}
          </ul>
        )}
      </section>

      {/* Add New Mapping */}
      <section className="bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-semibold mb-4">Add New Mapping</h2>

        {/* Tag ID Input */}
        <div className="mb-4">
          <label className="block text-sm font-medium mb-1">NFC Tag ID</label>
          <input
            type="text"
            value={tagId}
            onChange={(e) => setTagId(e.target.value)}
            placeholder="e.g. 04:A2:3B:5C:6D:7E:80"
            className="w-full border rounded px-3 py-2"
          />
        </div>

        {/* Spotify Search */}
        <div className="mb-4">
          <label className="block text-sm font-medium mb-1">
            Search Spotify
          </label>
          <div className="flex gap-2">
            <input
              type="text"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && handleSearch()}
              placeholder="Search for a song..."
              className="flex-1 border rounded px-3 py-2"
            />
            <button
              onClick={handleSearch}
              className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
            >
              Search
            </button>
          </div>
        </div>

        {/* Search Results */}
        {searchResults.length > 0 && (
          <div className="mb-4 max-h-60 overflow-y-auto">
            <ul className="space-y-1">
              {searchResults.map((track) => (
                <li
                  key={track.uri}
                  onClick={() => setSelectedTrack(track)}
                  className={`flex items-center gap-3 p-2 rounded cursor-pointer hover:bg-gray-100 ${
                    selectedTrack?.uri === track.uri
                      ? "bg-green-50 border border-green-300"
                      : ""
                  }`}
                >
                  {track.image_url && (
                    <img
                      src={track.image_url}
                      alt=""
                      className="w-10 h-10 rounded"
                    />
                  )}
                  <div>
                    <p className="text-sm font-medium">{track.name}</p>
                    <p className="text-xs text-gray-500">{track.artist}</p>
                  </div>
                </li>
              ))}
            </ul>
          </div>
        )}

        {/* Selected Track */}
        {selectedTrack && (
          <div className="mb-4 p-3 bg-green-50 rounded">
            Selected: <strong>{selectedTrack.name}</strong> by{" "}
            {selectedTrack.artist}
          </div>
        )}

        <button
          onClick={handleCreate}
          disabled={!tagId.trim() || !selectedTrack}
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          Save Mapping
        </button>
      </section>
    </main>
  );
}
