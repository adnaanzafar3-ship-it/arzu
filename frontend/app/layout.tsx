import type { Metadata } from "next";
import "./globals.css";
import Header from "../components/Header";
import Footer from "../components/Footer";

export const metadata: Metadata = {
 title: { default:"Padhaanewala — Find the Right College for Your Future", template:"%s | Padhaanewala" },
 description:"Find colleges, courses, scholarships, exams and education assistance with Padhaanewala.",
 metadataBase:new URL("https://padhaanewala.in")
};

export default function RootLayout({children}:{children:React.ReactNode}){
 return <html lang="en"><body><Header/><main>{children}</main><Footer/></body></html>
}
