import Link from "next/link";
export default function Footer(){
 return <footer className="bg-slate-950 text-white mt-16">
  <div className="container py-10 grid md:grid-cols-4 gap-8">
   <div><h3 className="font-bold text-xl">Padhaanewala</h3><p className="text-slate-300 mt-2">College discovery, education guidance and admission assistance.</p></div>
   <div><h4 className="font-bold">Explore</h4><div className="grid gap-2 mt-2 text-slate-300"><Link href="/colleges">Colleges</Link><Link href="/courses">Courses</Link><Link href="/scholarships">Scholarships</Link></div></div>
   <div><h4 className="font-bold">Students</h4><div className="grid gap-2 mt-2 text-slate-300"><Link href="/predictor">College Predictor</Link><Link href="/mock-tests">Mock Tests</Link><Link href="/exams">Exams</Link></div></div>
   <div><h4 className="font-bold">Company</h4><div className="grid gap-2 mt-2 text-slate-300"><Link href="/about">About</Link><Link href="/contact">Contact</Link><Link href="/privacy">Privacy</Link><Link href="/terms">Terms</Link></div></div>
  </div>
  <div className="border-t border-slate-800 py-5 text-center text-slate-400 text-sm">© {new Date().getFullYear()} Padhaanewala Edutech Services. All rights reserved.</div>
 </footer>
}
