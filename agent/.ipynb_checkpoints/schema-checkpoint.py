"""
Definisi Tipe Data, Model State, dan Skema Interaksi Kognitif.
Menggunakan Pydantic untuk penjaminan tipe data run-time yang kokoh.
"""
from typing import List, Optional, Literal, Dict, Any
from pydantic import BaseModel, Field

class IncidentTicket(BaseModel):
    ticket_id: str = Field(..., description="ID Unik Tiket Insiden")
    service_name: str = Field(..., description="Nama mikroservis yang terdampak")
    severity: Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"] = Field(..., description="Tingkat keparahan")
    error_message: str = Field(..., description="Deskripsi keluhan atau log awal")
    reported_at: str = Field(..., description="Stempel waktu pelaporan")

class AgentStep(BaseModel):
    iteration: int
    thought: str = Field(..., description="Penalaran kognitif agen sebelum mengambil aksi")
    action_name: str = Field(..., description="Nama tool yang dipanggil")
    action_params: Dict[str, Any] = Field(default_factory=dict, description="Parameter eksekusi tool")
    observation: str = Field(..., description="Hasil nyata yang dikembalikan oleh lingkungan/tool")

class IncidentResolution(BaseModel):
    ticket_id: str
    status: Literal["RESOLVED", "ESCALATED_TO_HUMAN", "FAILED"]
    root_cause: str
    actions_executed: List[str]
    verification_metrics: str
    executive_summary: str
    execution_steps: List[AgentStep]