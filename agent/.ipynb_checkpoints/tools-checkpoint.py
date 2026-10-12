"""
Pustaka Perkakas (Tool Registry) untuk Diagnostik dan Remediasi Server SRE.
Menyediakan operasi deterministik dan simulasi kondisi sistem nyata.
"""
import json
from typing import Dict, Any

class SystemToolRegistry:
    
    # State mock server internal untuk simulasi dunia nyata
    _mock_server_state = {
        "auth-service": {"cpu_percent": 34.2, "memory_percent": 94.8, "status": "DEGRADED", "pod_restarts": 12},
        "payment-gateway": {"cpu_percent": 98.1, "memory_percent": 78.4, "status": "CRITICAL", "pod_restarts": 1},
        "order-processor": {"cpu_percent": 15.0, "memory_percent": 41.2, "status": "HEALTHY", "pod_restarts": 0},
    }

    @classmethod
    def query_system_metrics(cls, service_name: str) -> str:
        """Mengambil data telemetri waktu-nyata (CPU, RAM, Status, Restarts) dari target layanan."""
        metrics = cls._mock_server_state.get(service_name)
        if not metrics:
            return json.dumps({"error": f"Layanan '{service_name}' tidak ditemukan pada kluster k8s."})
        return json.dumps({
            "service": service_name,
            "metrics": metrics,
            "telemetry_source": "Prometheus/NodeExporter"
        })

    @classmethod
    def fetch_service_logs(cls, service_name: str, lines_count: int = 5) -> str:
        """Mengambil log konsol terakhir dari container pod terkait."""
        if service_name == "auth-service":
            return json.dumps([
                "[ERROR] java.lang.OutOfMemoryError: Java heap space",
                "[WARN] GC overhead limit exceeded in worker thread pool",
                "[ERROR] Failed to obtain lock on redis session store: Timeout 3000ms",
                "[INFO] Incoming auth request count: 2400 req/sec",
                "[FATAL] Health check probe failed on port 8080"
            ])
        elif service_name == "payment-gateway":
            return json.dumps([
                "[WARN] Database connection pool saturated (active=100, max=100)",
                "[ERROR] Deadlock detected during transaction serialization",
                "[ERROR] HTTP 504 Gateway Timeout from core banking upstream",
                "[WARN] Retry queue exhausted for TX-882910",
                "[ERROR] Health check latency > 5000ms"
            ])
        else:
            return json.dumps(["[INFO] Semua proses beroperasi dalam ambang batas normal."])

    @classmethod
    def purge_redis_cache(cls, service_name: str) -> str:
        """Membersihkan alokasi memori cache Redis yang menumpuk atau mengalami stale lock."""
        if service_name in cls._mock_server_state:
            cls._mock_server_state[service_name]["memory_percent"] = 42.1
            return json.dumps({
                "action": "purge_redis_cache",
                "service": service_name,
                "status": "SUCCESS",
                "cleared_keys_count": 14280,
                "freed_memory_mb": 1024
            })
        return json.dumps({"error": "Gagal membersihkan cache: Layanan tidak valid."})

    @classmethod
    def restart_service_pod(cls, service_name: str) -> str:
        """Melakukan rolling restart pod secara aman pada orkestrator kontainer Kubernetes."""
        if service_name in cls._mock_server_state:
            cls._mock_server_state[service_name]["status"] = "HEALTHY"
            cls._mock_server_state[service_name]["cpu_percent"] = 18.5
            cls._mock_server_state[service_name]["memory_percent"] = 45.0
            cls._mock_server_state[service_name]["pod_restarts"] += 1
            return json.dumps({
                "action": "restart_service_pod",
                "service": service_name,
                "status": "ROLLING_RESTART_COMPLETED",
                "healthy_replicas": "3/3"
            })
        return json.dumps({"error": "Gagal me-restart: Pod tidak terdeteksi."})

    @classmethod
    def search_sre_knowledgebase(cls, query: str) -> str:
        """Melakukan pencarian solusi standar pada buku panduan operasional (Runbook) SRE."""
        query_lower = query.lower()
        if "outofmemory" in query_lower or "memory" in query_lower:
            return json.dumps({
                "runbook_id": "RB-042",
                "recommended_sequence": ["query_system_metrics", "purge_redis_cache", "restart_service_pod"],
                "mitigation": "Bersihkan stale cache session terlebih dahulu, lalu eksekusi rolling restart."
            })
        elif "deadlock" in query_lower or "database" in query_lower:
            return json.dumps({
                "runbook_id": "RB-108",
                "recommended_sequence": ["query_system_metrics", "fetch_service_logs"],
                "mitigation": "Masalah database deadlock memerlukan intervensi manual DBA jika upstream gagal."
            })
        return json.dumps({"message": "Tidak ada panduan otomatis yang cocok persis. Butuh eskalasi."})

    @classmethod
    def execute_tool(cls, tool_name: str, **kwargs) -> str:
        """Pintu masuk eksekusi perkakas secara dinamis dengan penanganan pengecualian."""
        available_tools = {
            "query_system_metrics": cls.query_system_metrics,
            "fetch_service_logs": cls.fetch_service_logs,
            "purge_redis_cache": cls.purge_redis_cache,
            "restart_service_pod": cls.restart_service_pod,
            "search_sre_knowledgebase": cls.search_sre_knowledgebase,
        }
        
        if tool_name not in available_tools:
            return json.dumps({"error": f"Tool '{tool_name}' tidak terdaftar dalam kapabilitas agen."})
        
        try:
            return available_tools[tool_name](**kwargs)
        except Exception as e:
            return json.dumps({"error": f"Pengecualian eksekusi tool '{tool_name}': {str(e)}"})