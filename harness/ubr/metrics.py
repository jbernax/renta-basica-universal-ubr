"""Deterministic plan metrics that complement the judge's rubric scores."""
from __future__ import annotations

from ubr.plan_model import citable_documents, extract_citations, load_modules, load_sources, word_count
from ubr.project import Project


def compute_metrics(project: Project) -> dict:
    modules = load_modules(project)
    factor_ids = [f["id"] for f in project.factors]
    covered = {
        factor
        for m in modules
        if m.research_questions
        for factor in (m.meta.get("covers") or [])
    }
    sources = {s["id"]: s for s in load_sources(project)}
    cited: set[str] = set()
    for doc in citable_documents(project):
        cited.update(extract_citations(doc.read_text(encoding="utf-8")))
    cited_known = cited & set(sources)
    verified = {sid for sid in cited_known if sources[sid].get("verified")}
    module_words = {m.id: word_count(m.body) for m in modules}
    module_citations = {m.id: len(extract_citations(m.body)) for m in modules}
    total_words = sum(module_words.values())

    return {
        "modules": len(modules),
        "locked_modules": sum(1 for m in modules if m.locked),
        "factors_total": len(factor_ids),
        "coverage": len(covered & set(factor_ids)) / len(factor_ids) if factor_ids else 1.0,
        "uncovered_factors": [f for f in factor_ids if f not in covered],
        "sources_total": len(sources),
        "cited_sources": len(cited_known),
        "verified_ratio": len(verified) / len(cited_known) if cited_known else 0.0,
        "unverified_cited": sorted(cited_known - verified),
        "research_questions": {m.id: len(m.research_questions) for m in modules},
        "research_questions_total": sum(len(m.research_questions) for m in modules),
        "words_total": total_words,
        "citations_per_1k_words": round(1000 * sum(module_citations.values()) / total_words, 2) if total_words else 0.0,
        "thin_modules": sorted(mid for mid, n in module_citations.items() if n < 3),
    }
