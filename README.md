# SaaS Document Anonymizer

A privacy-first SaaS platform for automated document anonymization. Upload documents in various formats, detect and review sensitive information, customize anonymization, and export redacted files securely. Built for legal, healthcare, research, and compliance professionals.

---

## 🚀 Features
- **Multi-format Upload**: Supports PDF, DOCX, TXT, and more.
- **Sensitive Data Detection**: Identifies addresses, phones, emails, names, and custom types.
- **Customizable Anonymization**: Select which types of information to redact.
- **Review & Export**: See detected items, export lists (CSV/JSON), and download anonymized documents.
- **API-first**: Integrate with your own tools or workflows.
- **Markdown-based UI**: Use MDX to blend Markdown and React for a declarative, content-driven interface.
- **Configurable UI**: Define UI behavior declaratively with JSON or YAML.
- **Privacy by Design**: No unnecessary data retention, encrypted processing, GDPR-ready.

---

## 🏗️ Architecture
- **Backend**: Python (FastAPI), containerized with Docker.
- **Frontend**: Next.js (App Router), shadcn/ui, Tailwind CSS, MDX for content, Zustand or TanStack Query for state/data, NextAuth.js for authentication.
- **Cloud-native**: Deployable to AWS ECS Fargate, Google Cloud Run, or similar.
- **CI/CD**: Automated with GitHub Actions (Docker image builds, tests, deployments).

### High-level Diagram
```
User ──▶ Next.js (MDX UI) ──▶ API (Docker) ──▶ Cloud Processing & Storage
```

---

## 🛠️ Tech Stack
| Layer            | Technology                                  | Why                                                     |
| ---------------- | ------------------------------------------- | ------------------------------------------------------- |
| Framework        | **Next.js (App Router)**                    | Best performance, SSR/ISR, built-in API routes          |
| UI & Styling     | **shadcn/ui + Tailwind CSS**                | Fast, clean, accessible components out-of-the-box       |
| Content          | **MDX**                                     | Blend Markdown and React declaratively                  |
| State Management | **Zustand** or **TanStack Query**           | Lightweight and scalable state/data layer               |
| File Handling    | `<input type="file" />` + Next.js API route | Native file uploads, no external service needed         |
| Auth             | **NextAuth.js**                             | Secure, plug-and-play authentication (OAuth, JWT, etc.) |
| Config           | JSON or YAML                                | Use to define UI behavior declaratively                 |

- **Backend**: Python, FastAPI, Presidio, spaCy, Docker
- **Cloud**: AWS ECS Fargate (or GCP/Azure equivalents), S3, CloudFront
- **CI/CD**: GitHub Actions, Docker Hub/ECR
- **Payments**: Stripe

---

## 🗂️ Project Structure

```
Autonymous/
│
├── backend/                  # FastAPI backend (Dockerized)
│   ├── app/                  # Main API application code
│   │   ├── main.py           # FastAPI entrypoint
│   │   ├── api/              # API route definitions
│   │   ├── services/         # Business logic, anonymization, detection
│   │   ├── models/           # Pydantic models, schemas
│   │   └── utils/            # Utility functions
│   ├── tests/                # Backend tests
│   ├── Dockerfile            # Backend Dockerfile
│   └── requirements.txt      # Python dependencies
│
├── frontend/                 # Next.js (App Router) frontend
│   ├── app/                  # Next.js app directory (routing, pages)
│   ├── components/           # Reusable React components (shadcn/ui)
│   ├── styles/               # Tailwind CSS config and global styles
│   ├── content/              # MDX files for declarative UI/content
│   ├── config/               # JSON/YAML config for UI behavior
│   ├── state/                # Zustand or TanStack Query stores/hooks
│   ├── lib/                  # Utility functions, API clients
│   ├── public/               # Static assets (images, favicon, etc.)
│   ├── middleware/           # NextAuth.js and other middlewares
│   ├── tests/                # Frontend/component tests
│   ├── next.config.js        # Next.js configuration
│   └── tailwind.config.js    # Tailwind CSS configuration
│
├── .github/                  # GitHub Actions workflows, issue templates
├── docker-compose.yml        # (Optional) For local multi-service dev
├── LICENSE
├── README.md
└── SaaS_Document_Anonymizer_Roadmap.md
```

**Key Points:**
- **backend/**: All API logic, detection, anonymization, and Docker setup.
- **frontend/**: Next.js app, MDX content, shadcn/ui components, Tailwind CSS, config, and state management.
- **content/**: Write UI and documentation in MDX for a markdown-driven experience.
- **config/**: Use JSON or YAML to declaratively control UI and workflow.
- **.github/**: CI/CD, code quality, and community health files.

---

## ⚡ Quickstart (Local Development)

### Prerequisites
- [Docker](https://www.docker.com/get-started)
- [Node.js](https://nodejs.org/) (for frontend)

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Autonymous
```

### 2. Backend (API)
```bash
docker build -t anonymizer-api ./backend
# Run the API
# Example: docker run -p 8000:8000 anonymizer-api
```

### 3. Frontend (Web App)
```bash
cd frontend
npm install
npm run dev
```
- The UI is built with Next.js (App Router), shadcn/ui, Tailwind CSS, and MDX.
- Edit `.mdx` files in the `content/` directory to update UI content declaratively.
- UI configuration can be managed via JSON or YAML files in the `config/` directory.

### 4. Access
- API: http://localhost:8000/docs (Swagger UI)
- Web App: http://localhost:3000

---

## ☁️ Deployment
- **Production**: Build and push Docker images to a registry (ECR, Docker Hub).
- **Deploy API**: Use AWS ECS Fargate, Google Cloud Run, or Azure Container Apps.
- **Deploy Frontend**: Use Vercel, Netlify, or host as a static site via S3 + CloudFront. Next.js supports SSR/ISR and static export.
- **CI/CD**: Automated builds, tests, and deployments via GitHub Actions.

---

## 🔒 Security & Privacy
- All data in transit is encrypted (HTTPS/TLS).
- No persistent storage of user documents unless required (and always encrypted).
- Secrets managed via cloud secret managers.
- GDPR-ready: easy data deletion, no unnecessary retention.
- Audit logging for compliance (no document content logged).
- Authentication via NextAuth.js (OAuth, JWT, etc.).

---

## 🤝 Contributing
We welcome contributions! To get started:
1. Fork the repo and create a feature branch.
2. Follow the code style and add tests where relevant.
3. Open a pull request with a clear description.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details (to be created).

---

## 📄 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 📫 Contact & Support
For questions, feature requests, or support, please open an issue or contact the maintainer.
