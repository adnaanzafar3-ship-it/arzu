"use client";
import { useEffect,useState } from "react";
import { useParams } from "next/navigation";
import { api } from "../../../lib/api";
export default function CollegePage(){
 const p=useParams(); const [c,setC]=useState<any>(null);
 useEffect(()=>{if(p.id)api(`/api/v1/colleges/${p.id}`).then(setC)},[p.id]);
 if(!c)return <div className="container py-12">Loading...</div>;
 return <div className="container py-12"><div className="card"><span className="badge">{c.college_type}</span><h1 className="text-4xl font-black mt-4">{c.name}</h1><p className="text-slate-500 mt-2">{c.city}, {c.state}</p><div className="grid md:grid-cols-3 gap-4 mt-8"><div><b>Rating</b><p>⭐ {c.rating}</p></div><div><b>Hostel</b><p>{c.hostel?"Available":"Not listed"}</p></div><div><b>Established</b><p>{c.established_year||"Not listed"}</p></div></div><hr className="my-8"/><h2 className="text-2xl font-bold">Overview</h2><p className="mt-3 text-slate-600">{c.description||"College information will be updated by the administrator."}</p><h2 className="text-2xl font-bold mt-8">Facilities</h2><p className="mt-3 text-slate-600">{c.facilities||"Not listed"}</p><div className="mt-8"><a className="btn btn-primary" href="/#enquiry">Get Admission Assistance</a></div></div></div>
}
