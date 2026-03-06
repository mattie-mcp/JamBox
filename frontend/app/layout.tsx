import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "JamBox — Jamie's Music Box",
  description: "A smart NFC music player for Jamie. Tap a toy, play a song.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
