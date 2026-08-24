import type { MetadataRoute } from "next";
export default function sitemap(): MetadataRoute.Sitemap {
 const base="https://padhaanewala.in";
 return ["/","/colleges","/courses","/predictor","/scholarships","/exams","/mock-tests","/reviews","/blog","/about","/contact"].map(path=>({url:base+path,lastModified:new Date()}));
}
