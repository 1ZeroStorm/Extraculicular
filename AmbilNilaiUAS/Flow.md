

```mermaid
flowchart TD

subgraph Flow_Besar_Sistem [Flow Besar Sistem]
    A[User Browser] --> B[Halaman HTML]
    B --> C[Routing Flask/Django]
    C --> D[Proses Backend]
    D --> E[Database MySQL]
    E --> F[Response ke User]
end

subgraph Flow_Create [Flow Create]
    C1[User isi form] --> C2[Submit]
    C2 --> C3[Routing menerima POST]
    C3 --> C4[Simpan ke database]
    C4 --> C5[Redirect ke halaman list]
end

subgraph Flow_Read [Flow Read]
    R1[User buka halaman] --> R2[Routing dipanggil]
    R2 --> R3[Ambil data dari database]
    R3 --> R4[Tampilkan di tabel HTML]
end