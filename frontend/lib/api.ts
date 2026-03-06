const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export interface TagMapping {
  id: number;
  tag_id: string;
  spotify_uri: string;
  name: string;
  created_at: string;
}

export interface SpotifyTrack {
  uri: string;
  name: string;
  artist: string;
  image_url: string | null;
}

export async function fetchMappings(): Promise<TagMapping[]> {
  const res = await fetch(`${API_BASE}/api/mappings`);
  if (!res.ok) throw new Error("Failed to fetch mappings");
  return res.json();
}

export async function createMapping(data: {
  tag_id: string;
  spotify_uri: string;
  name: string;
}): Promise<TagMapping> {
  const res = await fetch(`${API_BASE}/api/mappings`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to create mapping");
  return res.json();
}

export async function deleteMapping(id: number): Promise<void> {
  const res = await fetch(`${API_BASE}/api/mappings/${id}`, {
    method: "DELETE",
  });
  if (!res.ok) throw new Error("Failed to delete mapping");
}

export async function searchTracks(query: string): Promise<SpotifyTrack[]> {
  const res = await fetch(
    `${API_BASE}/api/search?q=${encodeURIComponent(query)}`
  );
  if (!res.ok) throw new Error("Failed to search");
  return res.json();
}
