# GetaJob
![Python](https://img.shields.io/badge/Python-yellow)
![NextJS](https://img.shields.io/badge/NextJS-white)
![FastAPI](https://img.shields.io/badge/FastAPI-green)
![MongoDB](https://img.shields.io/badge/MongoDB-orange)
![Cloudinary](https://img.shields.io/badge/Cloudinary-blue)
![GroqCloud](https://img.shields.io/badge/GroqCloud-gray)
![OCR](https://img.shields.io/badge/OCR-purple)

> **GetaJob** adalah platform pencarian kerja modern berbasis AI yang mempermudah job seekers menemukan pekerjaan yang sesuai, serta membantu recruiters menyaring kandidat secara efisien.

Dengan teknologi **Resume Parsing**, **Job Recommendation**, **AI Matching**, dan sistem **Manajemen Job Posting** yang terintegrasi, GetaJob mempermudah proses seleksi dan pencocokan antara kandidat dan lowongan pekerjaan.
—


## Contributors
Ketua Kelompok: Muhammad Hilmi Dzaki Wismadi - 22/497591/TK/54539  
Anggota 1: Rama Sulaiman Nurcahyo - 22/492727/TK/53940  
Anggota 2: Flavia Hidayriamraata Pualam - 22/494376/TK/54219  
Anggota 3: Muhammad Hilmi Dzaki Wismadi - 22/497591/TK/54539

## Online Deployment
Aplikasi ini telah terdeploy pada situs berikut  
[Frontend : https://geta-job.vercel.app/](https://geta-job.vercel.app/)  
[Backend : https://unconscious-puma-universitas-gadjah-mada-f822e818.koyeb.app](https://unconscious-puma-universitas-gadjah-mada-f822e818.koyeb.app/docs#/)

##  Fitur Utama
### Untuk Job Seekers
- **Upload CV** (PDF) dan sistem akan mengekstrak informasi penting secara otomatis.
- **Pencocokan Otomatis** dengan lowongan berdasarkan keahlian, pengalaman, dan preferensi.
- **Rekomendasi Pekerjaan** personal yang diperbarui secara berkala.
- **Dashboard Lamaran** untuk memantau status aplikasi pekerjaan.

### Untuk Recruiters
- **Upload Lowongan Pekerjaan** dengan detail lengkap (judul, deskripsi, kualifikasi, dll).
- **AI Candidate Matching** untuk menyarankan pelamar yang paling relevan.
- **Resume Viewer** dengan parsing otomatis (dengan model NLP).
- **Manajemen Kandidat** dan status lamaran.

### Teknologi yang Digunakan
- **Frontend**: [Next.js](https://nextjs.org/)  
- **Backend**. [Python](https://www.python.org/)
- **Backend API**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: [MongoDB](https://www.mongodb.com/)
- **Storage**: [Cloudinary](https://cloudinary.com/) untuk manajemen foto profil dan file CV.
- **AI Features**: Resume parsing & job matching menggunakan LLM.

##  Instalasi & Penggunaan Lokal
### 1. Clone Repository
```bash
git clone https://github.com/hilmiwismadi/GetaJob.git
cd getajob
```

### 2. Setup Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Setup Frontend
```
cd frontend
npm install
```

### 4. Environment Variables
Buat *environment variable* di file.env  
**Frontend**
Letakkan di /frontend/.env:
```ini
# Public
NEXT_PUBLIC_API_URL="<Your Backend URL>"
NEXT_PUBLIC_CLOUDINARY_CLOUD_NAME="<Your Cloudinary Name>"

# Private
CLOUDINARY_CLOUD_NAME="<Your Cloudinary Name>"
CLOUDINARY_API_KEY="<Your Cloudinary API Key>"
CLOUDINARY_API_SECRET="<Your Cloudinary API Secret>"
```

**Backend**
Letakkan di /backend/app/.env
```ini
MONGODB_URI="<Your MONGODB URI (mongodb+srv…)>"
EMAIL_USER="<Email used for sending otp>"
EMAIL_PASSWORD="<Email password used for sending otp>"
JWT_SECRET_KEY="<Your Secure JWT Secret Key>"
GROQ_API_KEY="<Your Groq API Key>"
```

### 5. Menjalankan Situs Web  
**Backend**
1. Start the FastAPI server:  
In /backend/
   ```sh
   python -m app.api 
   ```

2. Open your browser and navigate to:
   - Interactive API docs: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Redoc API docs: [http://localhost:8000/redoc](http://localhost:8000/redoc)  

**Frontend**  
1. Start the Web server:  
In /frontend/
```sh
npm run dev
```
2. Open your browser and navigate to:
[http://localhost:3000](http://localhost:3000)

## Backend Endpoint  
### Appliers
- POST `/appliers/` Create Applier  
- GET `/appliers/` Get All Appliers  
- GET `/appliers/{applier_id}` Get Applier by Id  
- PUT `/appliers/{applier_id}` Update Applier (Authenticated)  
- DELETE `/appliers/{applier_id}` Delete Applier  
- GET `/appliers/username/{username}` Get Applier by Username  
- GET `/appliers/email/{email}` Get Applier by Email  
- PUT `/appliers/{applier_id}/clear-profile-picture` Clear Applier Profile Picture  
- PUT `/appliers/{applier_id}/update-resume` Update Applier Resume  
- PUT `/appliers/{applier_id}/delete-resume-components` Delete Applier Resume Components  
- POST `/appliers/{applier_id}/change-password` Change Password  
- GET `/appliers/search/` Search Appliers by Keyword  
### Recruiters
- POST `/recruiters/` Create Recruiter  
- GET `/recruiters/` Get Recruiter  
- GET `/recruiters/{recruiter_id}` Get Recruiter by Id  
- PUT `/recruiters/{recruiter_id}` Update Recruiter  
- DELETE `/recruiters/{recruiter_id}` Delete Recruiter  
- GET `/recruiters/username/{username}` Get Recruiter by Username  
- GET `/recruiters/email/{email}` Get Recruiter by Email  
- PUT `/recruiters/{recruiter_id}/clear-profile-picture` Clear Recruiter Profile Picture  
- POST `/recruiters/{recruiter_id}/change-password` Change Password  
- GET `/recruiters/search/` Search Recruiter by Keyword
### Jobs
- POST `/jobs/` Create Job  
- GET `/jobs/` Get All Jobs  
- GET `/jobs/{job_id}` Get Job by Id  
- PUT `/jobs/{job_id}` Update Job  
- DELETE `/jobs/{job_id}` Delete Job  
- GET `/jobs/recruiter/{recruiter_id}` Get Jobs by Recruiter  
- GET `/jobs/search/` Search Jobs by Keyword  
- GET `/jobs/search/image` Search Jobs by Keyword Containing Profile Picture  
- GET `/jobs/image/` Get All Jobs with its Recruiter Profile Picture  
- GET `/jobs/image/count` Get Jobs Count  
- GET `/jobs/recruiter/{recruiter_id}/count` Get a Recruiter Jobs Total Count  
### Job Applications
- POST `/applications/` Create Applications  
- GET `/applications/{application_id}` Get Application by Id  
- PUT `/applications/{application_id}` Update Application  
- DELETE `/applications/{application_id}` Delete Application  
- GET `/applications/history/{applier_id}` Get Applier Job History  
- GET `/applications/job/{job_id}/appliers` Get Applier by Job Id  
- GET `/applications/job/{job_id}/count` Get Applier Count by Job Id  
- GET `/applications/applier/{applier_id}/count` Get Job Count by Applier Id
### Resume
- POST `/resume/parse/image_text` Extract Text from PDF using OCR  
- POST `/resume/parse/pdf_text` Extract Text from PDF Without OCR  
- GET `/resume/applier/rate` Get Applier Resume Rating  
- GET `/resume/recruiter/rate` Get Recruiter Suggestion for Applier Resume  
- GET `/resume/applier/ask` Get Recommendation Whether a Job is Fit
### Recommendations
- POST `/recommendations/cluster/applierdbscan` Refresh Cluster using DBSCAN  
- POST `/recommendations/cluster/applierkmeans` Refresh Cluster using K-means  
- GET `/recommendations/applier/{applier_id}` Get Applier Recommendations
### Authentication
- POST `/auth/login` Login  
- POST `/auth/refresh` Refresh Token  
- GET `/auth/me` Get Current User  
- POST `/auth/forgot-password` Forgot Password  
- POST `/auth/verify-otp` Verify OTP  
- POST `/auth/reset-password` Reset Password
### LogViews
- POST `/log-views/` Create Log View  
- GET `/log-views/applier/{applier_id}` Get Logs by Applier  
- GET `/log-views/applier/{applier_id}/count` Get Log Count by Applier  
- GET `/log-views/job/{job_id}/count` Get Log Count by Job  
- GET `/log-views/job/{job_id}` Get Logs by Job Id
## Kontak
Jika ada pertanyaan atau kolaborasi, silakan hubungi melalui GitHub Issue atau email resmi.


