
# Cache Baseline Report — 12-Oct-2026

## Objective
Measure performance with caching disabled and enabled for the Department Employee Statistics API.

## Endpoint
GET /api/v1/departments/stats/

## Performance Results

| Metric | Cache OFF | Cache ON |
|---|---:|---:|
| Average response time | 21.55 ms | 0.32 ms |
| Minimum response time | 2.41 ms | 0.30 ms |
| Maximum response time | 193.25 ms | 0.32 ms |
| Iterations | 10 | 10 |

## Conclusion
The average execution time was 21.55 ms without cached results and 0.32 ms with cached results. The cached path was approximately 67 times faster in this test.

## Cache Design

- Cache key: `department_employee_stats_v1`
- TTL: 300 seconds (5 minutes)
- Invalidation: Delete cached statistics after employee creation, update, deletion, and transfer.
- Freshness: After invalidation, the next request should fetch updated statistics and cache the new result.

## Notes
These are local test measurements. Performance may vary depending on system load, database performance, and Redis availability.
