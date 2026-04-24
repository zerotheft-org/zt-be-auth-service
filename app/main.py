from fastapi import FastAPI
from common.telemetry import configure_telemetry, instrument_app

app = FastAPI()

# Configure OpenTelemetry
configure_telemetry()

@app.get("/")
def root():
    return {
        "message": "Welcome to Auth Service!",
        "version": "0.1.0",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Auth Service",
        "environment": "development"
    }

# Instrument FastAPI app with OpenTelemetry
instrument_app(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
