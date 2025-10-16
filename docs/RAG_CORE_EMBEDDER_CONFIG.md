# RAG Core - Nomic Embedder Configuration

## Overview
The RAG Core (Manual Oracle) now uses the **Nomic Embed Text v1.5** model via LM Studio API for semantic search and similarity matching.

## Model Information

**Model:** `nomic-ai/nomic-embed-text-v1.5-GGUF`  
**File:** `nomic-embed-text-v1.5.Q4_K_M.gguf`  
**Format:** GGUF  
**Quantization:** Q4_K_M  
**Architecture:** nomic-bert  
**Domain:** embedding  
**Size on Disk:** 84.11 MB  
**Embedding Dimension:** 768

## Features

### 1. LM Studio API Integration
- **Endpoint:** `http://localhost:1234/v1/embeddings`
- **Model:** Loaded in LM Studio
- **Timeout:** 10 seconds per request
- **Text Limit:** 4000 characters per embedding

### 2. Graceful Degradation
- **Connection Test:** Validates LM Studio API on initialization
- **Fallback Mode:** If connection fails, Oracle uses regex-only search
- **Error Handling:** Silently falls back to exact text matching

### 3. Two-Pass Search
1. **First Pass:** Exact text/regex matching (fast)
2. **Second Pass:** Embedding-based semantic search (if embedder available)

## Usage

### Basic Search
```bash
py main.py --rag search "How do I use Luna?"
```

**Output:**
```
Found 5 results:
  1. Using the System (Score: 0.650)
  2. Using Benchmarks (Score: 0.580)
  3. Monitoring and Performance (Score: 0.486)
```

### Subsystem-Specific Search
```bash
py main.py --rag search "memory optimization" --subsystem carma
```

### Test RAG Core
```bash
py main.py --rag test
```

## Integration with Audit System

### Oracle Check
The Oracle Check in the V3 Sovereign audit system now has access to semantic search:

1. **Finding Enhancement:** Adds relevant manual citations to audit findings
2. **Semantic Matching:** Uses embeddings to find related sections
3. **Similarity Scores:** Ranks results by relevance (0.0-1.0)
4. **Subsystem Filtering:** Only searches relevant core subsystems

### Example Citation
```python
finding = {
    'issue_type': 'critical',
    'file_path': 'carma_core/carma_core.py',
    'verdict': 'FAIL',
    'issue_id': 'CRITICAL_001'
}

enhanced = oracle_check.enhance_finding_with_citation(finding, 'carma')
# Result includes citations with similarity scores
```

## Performance

### Initialization Time
- **First Load:** ~1-2 seconds (LM Studio connection test)
- **Subsequent Loads:** <100ms (cached connection)

### Search Performance
- **Exact Match:** <10ms (regex-based)
- **Embedding Search:** 100-500ms per section (depends on LM Studio)
- **Full Manual Search:** 2-5 seconds (49 sections)

### Memory Usage
- **Manual Memory Map:** ~2MB (AIOS_MANUAL.md)
- **Oracle Index:** <1MB (49 sections)
- **Embeddings:** Generated on-demand (not cached)

## Configuration

### LM Studio Setup
1. **Load Model:** `nomic-embed-text-v1.5.Q4_K_M.gguf`
2. **Start Server:** Ensure LM Studio is running on port 1234
3. **Test Connection:** `py main.py --rag test`

### Manual Oracle Settings
Located in `rag_core/manual_oracle.py`:

```python
self.lm_studio_url = "http://localhost:1234"
self.embedding_model = "nomic-ai/nomic-embed-text-v1.5-GGUF"
self.embedding_dim = 768  # Nomic embedding dimension
```

### Fallback Behavior
If LM Studio is not available:
- Oracle continues to work with regex-only search
- Warning message displayed on initialization
- No semantic search capabilities

## Testing

### Test Embedder Connection
```bash
py scripts/test_oracle_citations.py
```

### Test RAG Search
```bash
py main.py --rag search "test query"
```

### Test Full Audit with Oracle
```bash
py main.py --audit --v3
```

## Troubleshooting

### Connection Errors
**Error:** "Could not connect to LM Studio"  
**Solution:** 
1. Ensure LM Studio is running
2. Verify model is loaded
3. Check port 1234 is available

### Slow Search Performance
**Issue:** Embedding search takes >5 seconds  
**Solution:**
1. Reduce text length (Oracle limits to 4000 chars)
2. Use exact text search for known terms
3. Check LM Studio resource usage

### No Results Found
**Issue:** Search returns empty results  
**Solution:**
1. Try exact text search first
2. Verify query is relevant to manual content
3. Check subsystem filter (if used)

## Future Enhancements

### Potential Improvements
1. **Embedding Cache:** Cache section embeddings to disk
2. **Batch Processing:** Process multiple sections in one API call
3. **Hybrid Search:** Combine exact + embedding scores
4. **Query Expansion:** Use LLM to expand queries
5. **Re-ranking:** Post-process results with cross-encoder

### Performance Optimizations
1. **Lazy Loading:** Only embed sections when needed
2. **Smart Caching:** Cache frequently accessed embeddings
3. **Parallel Processing:** Multiple embedding requests simultaneously
4. **Index Optimization:** Pre-compute common query embeddings

---

**Last Updated:** 2025-10-15  
**Version:** 1.0  
**Status:** ✅ Operational with Nomic Embed Text v1.5
