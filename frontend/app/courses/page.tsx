"use client";
import { useEffect,useState } from "react";
import Link from "next/link";
import { api } from "../../lib/api";
export default function Courses(){const [x,setX]=useState<any[]>([]);useEffect(()=>{api<any[]>("/api/v1/courses").then(setX)},[]);return <div className="container py-12"><h1 className="text-4xl font-black">Courses</h1><div className="grid md:grid-cols-2 lg:grid-cols-3 gap-5 mt-8">{x.map(c=><Link className="card" href={`/courses/${c.slug}`} key={c.id}><h2 className="text-xl font-bold">{c.name}</h2><p className="text-slate-500 mt-2">{c.duration}</p><p className="mt-3">{c.eligibility}</p><span className="text-teal-700 font-bold inline-block mt-4">View course →</span></Link>)}</div></div>}
