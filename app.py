from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse, RedirectResponse
from uvicorn import run as app_run
from dotenv import load_dotenv
from typing import Optional

# Importing constants and pipeline modules from the project
from src.constants import APP_HOST, APP_PORT
from src.pipline.prediction_pipeline import CreditCardData, CreditCardDataClassifier
from src.pipline.training_pipeline import TrainingPipeline

load_dotenv()

app=FastAPI()

# Mount the 'static' directory for serving static files (like CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 template engine for rendering HTML templates
templates = Jinja2Templates(directory='templates')

origins = ["*"]

# Configure middleware to handle CORS, allowing requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class DataForm:

    def __init__(self, request: Request):
        self.request: Request = request
        self.Time: Optional[int] = None
        self.V1: Optional[float] = None
        self.V2: Optional[float] = None
        self.V3: Optional[float] = None
        self.V4: Optional[float] = None
        self.V5: Optional[float] = None
        self.V6: Optional[float] = None
        self.V7: Optional[float] = None
        self.V8: Optional[float] = None
        self.V9: Optional[float] = None
        self.V10: Optional[float] = None
        self.V11: Optional[float] = None
        self.V12: Optional[float] = None
        self.V13: Optional[float] = None
        self.V14: Optional[float] = None
        self.V15: Optional[float] = None
        self.V16: Optional[float] = None
        self.V17: Optional[float] = None
        self.V18: Optional[float] = None
        self.V19: Optional[float] = None
        self.V20: Optional[float] = None
        self.V21: Optional[float] = None
        self.V22: Optional[float] = None
        self.V23: Optional[float] = None
        self.V24: Optional[float] = None
        self.V25: Optional[float] = None
        self.V26: Optional[float] = None
        self.V27: Optional[float] = None
        self.V28: Optional[float] = None
        self.Amount: Optional[int] = None
        self.Hour: Optional[int] = None
        self.Time_diff: Optional[float] = None

    async def get_credit_Card_data(self):
        form = await self.request.form()

        self.Time = float(form.get("Time"))

        self.V1 = float(form.get("V1"))
        self.V2 = float(form.get("V2"))
        self.V3 = float(form.get("V3"))
        self.V4 = float(form.get("V4"))
        self.V5 = float(form.get("V5"))
        self.V6 = float(form.get("V6"))
        self.V7 = float(form.get("V7"))
        self.V8 = float(form.get("V8"))
        self.V9 = float(form.get("V9"))
        self.V10 = float(form.get("V10"))
        self.V11 = float(form.get("V11"))
        self.V12 = float(form.get("V12"))
        self.V13 = float(form.get("V13"))
        self.V14 = float(form.get("V14"))
        self.V15 = float(form.get("V15"))
        self.V16 = float(form.get("V16"))
        self.V17 = float(form.get("V17"))
        self.V18 = float(form.get("V18"))
        self.V19 = float(form.get("V19"))
        self.V20 = float(form.get("V20"))
        self.V21 = float(form.get("V21"))
        self.V22 = float(form.get("V22"))
        self.V23 = float(form.get("V23"))
        self.V24 = float(form.get("V24"))
        self.V25 = float(form.get("V25"))
        self.V26 = float(form.get("V26"))
        self.V27 = float(form.get("V27"))
        self.V28 = float(form.get("V28"))

        self.Amount = float(form.get("Amount"))
        self.Hour = float(form.get("Hour"))
        self.time_diff = float(form.get("time_diff"))
# Route to render the main page with the form
@app.get("/", tags=["authentication"])
async def index(request: Request):
    """
    Renders the main HTML form page for vehicle data input.
    """
    return templates.TemplateResponse(
        name="vehicledata.html",
        context={"request": request, "context": "Rendering"}
    )


# Route to trigger the model training process
@app.get("/train")
async def trainRouteClient():
    """
    Endpoint to initiate the model training pipeline.
    """
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_trainingpipeline()
        return Response("Training successful!!!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")

# Route to handle form submission and make predictions
@app.post("/")
async def predictRouteClient(request: Request):
    """
    Endpoint to receive form data, process it, and make a prediction.
    """
    try:
        form = DataForm(request)
        await form.get_credit_Card_data()
        
        credit_card_data = CreditCardData(
                        Time=form.Time,
                        V1=form.V1, V2=form.V2, V3=form.V3, V4=form.V4,
                        V5=form.V5, V6=form.V6, V7=form.V7, V8=form.V8,
                        V9=form.V9, V10=form.V10, V11=form.V11, V12=form.V12,
                        V13=form.V13, V14=form.V14, V15=form.V15, V16=form.V16,
                        V17=form.V17, V18=form.V18, V19=form.V19, V20=form.V20,
                        V21=form.V21, V22=form.V22, V23=form.V23, V24=form.V24,
                        V25=form.V25, V26=form.V26, V27=form.V27, V28=form.V28,
                        Amount=form.Amount,
                        Hour=form.Hour,
                        time_diff=form.time_diff
                )
        
        # Convert form data into a DataFrame for the model
        credit_card_df = credit_card_data.get_CreditCard_data_frame()

        # Initialize the prediction pipeline
        model_predictor = CreditCardDataClassifier()

        # Make a prediction and retrieve the result
        value = model_predictor.predict(dataframe=credit_card_df)[0]

        # Interpret the prediction result as 'Response-Yes' or 'Response-No'
        status = "Fraud" if value == 1 else "Normal"

        # Render the same HTML page with the prediction result
        return templates.TemplateResponse(
            name="vehicledata.html",
            context={"request": request, "context": status}
        )
        
    except Exception as e:
        return {"status": False, "error": f"{e}"}


if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=5000)