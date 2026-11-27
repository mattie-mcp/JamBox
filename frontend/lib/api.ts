// The built UI is served by the same FastAPI that serves the API, so calls are
// same-origin (""). `npm run dev` runs on :3000 and talks to a local API on :8000.
const API_BASE =
  process.env.NEXT_PUBLIC_API_URL ??
  (process.env.NODE_ENV === "development" ? "http://localhost:8000" : "");

export async function checkHealth(): Promise<boolean> {
  try {
    const res = await fetch(`${API_BASE}/health`, { signal: AbortSignal.timeout(3000) });
    return res.ok;
  } catch {
    return false;
  }
}

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

// --- Tags ---

export interface Tag {
  id: number;
  tag_id: string;
  friendly_name: string;
  created_at: string;
}

export interface DiscoveryStatus {
  active: boolean;
  detected_tag_id: string | null;
  seconds_remaining: number | null;
}

export async function fetchTags(): Promise<Tag[]> {
  const res = await fetch(`${API_BASE}/api/tags`);
  if (!res.ok) throw new Error("Failed to fetch tags");
  return res.json();
}

export async function fetchUnassignedTags(): Promise<Tag[]> {
  const res = await fetch(`${API_BASE}/api/tags/unassigned`);
  if (!res.ok) throw new Error("Failed to fetch unassigned tags");
  return res.json();
}

export async function createTag(data: {
  tag_id: string;
  friendly_name: string;
}): Promise<Tag> {
  const res = await fetch(`${API_BASE}/api/tags`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to create tag");
  return res.json();
}

export async function deleteTag(tagId: string): Promise<void> {
  const res = await fetch(`${API_BASE}/api/tags/${tagId}`, {
    method: "DELETE",
  });
  if (!res.ok) throw new Error("Failed to delete tag");
}

export async function startDiscovery(): Promise<{
  status: string;
  timeout_seconds: number;
}> {
  const res = await fetch(`${API_BASE}/api/discover/start`, {
    method: "POST",
  });
  if (!res.ok) throw new Error("Failed to start discovery");
  return res.json();
}

export async function getDiscoveryStatus(): Promise<DiscoveryStatus> {
  const res = await fetch(`${API_BASE}/api/discover/status`);
  if (!res.ok) throw new Error("Failed to get discovery status");
  return res.json();
}

export async function stopDiscovery(): Promise<void> {
  const res = await fetch(`${API_BASE}/api/discover/stop`, {
    method: "POST",
  });
  if (!res.ok) throw new Error("Failed to stop discovery");
}
