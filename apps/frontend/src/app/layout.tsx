import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "MM Matching App",
  description: "멘토-멘티 매칭 서비스",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ko">
      <body>{children}</body>
    </html>
  );
}
