import tkinter
from LungCancer_Model import lung_cancer_model_prediction


class LungCancer_GUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Lung Cancer Predictor")
        self.main_window.geometry("1350x750")

        # Create frames
        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        self.frame6 = tkinter.Frame(self.main_window)
        self.frame7 = tkinter.Frame(self.main_window)
        self.frame8 = tkinter.Frame(self.main_window)
        self.frame9 = tkinter.Frame(self.main_window)
        self.frame10 = tkinter.Frame(self.main_window)
        self.frame11 = tkinter.Frame(self.main_window)
        self.frame12 = tkinter.Frame(self.main_window)
        self.frame13 = tkinter.Frame(self.main_window)
        self.frame14 = tkinter.Frame(self.main_window)
        self.frame15 = tkinter.Frame(self.main_window)
        self.frame16 = tkinter.Frame(self.main_window)
        self.frame17 = tkinter.Frame(self.main_window)
        self.frame18 = tkinter.Frame(self.main_window)
        self.frame19 = tkinter.Frame(self.main_window)
        self.frame20 = tkinter.Frame(self.main_window)
        self.frame21 = tkinter.Frame(self.main_window)
        self.frame22 = tkinter.Frame(self.main_window)
        self.frame23 = tkinter.Frame(self.main_window)
        self.frame24 = tkinter.Frame(self.main_window)
        self.frame25 = tkinter.Frame(self.main_window)

        # Create Header
        self.header = tkinter.Label(self.frame1, text="Lung Cancer Predictor", font=("Helvetica bold", 40), fg="white",
                                    bg="blue")
        self.header.pack(pady=(40, 0))

        # Display accuracy
        self.arrest_accuracy = tkinter.Label(self.frame2,
                                             text=f"This prediction has an accuracy of: {lung_cancer_model_prediction.model_accuracy:.0%}",
                                             font=("Helvetica", 20))
        self.arrest_accuracy.pack()

        # Create labels, entry fields and a button
        self.label1 = tkinter.Label(self.frame2, text="Enter your age:", font=("Helvetica bold", 10))
        self.entry1 = tkinter.Entry(self.frame2, width=20)
        self.label1.pack(side="left")
        self.entry1.pack(side="left")

        self.label2 = tkinter.Label(self.frame3, text="Enter your gender (1: Male, 2: Female):",
                                    font=("Helvetica bold", 10))
        self.entry2 = tkinter.Entry(self.frame3, width=20)
        self.label2.pack(side="left")
        self.entry2.pack(side="left")

        self.label3 = tkinter.Label(self.frame4, text="Enter air pollution level (1-8):", font=("Helvetica bold", 10))
        self.entry3 = tkinter.Entry(self.frame4, width=20)
        self.label3.pack(side="left")
        self.entry3.pack(side="left")

        self.label4 = tkinter.Label(self.frame5, text="Enter your alcohol usage (1-8):", font=("Helvetica bold", 10))
        self.entry4 = tkinter.Entry(self.frame5, width=20)
        self.label4.pack(side="left")
        self.entry4.pack(side="left")

        self.label5 = tkinter.Label(self.frame6, text="Rate your dust allergy level (1-8):",
                                    font=("Helvetica bold", 10))
        self.entry5 = tkinter.Entry(self.frame6, width=20)
        self.label5.pack(side="left")
        self.entry5.pack(side="left")

        self.label6 = tkinter.Label(self.frame7, text="Rate your occupational hazardous level (1-8):",
                                    font=("Helvetica bold", 10))
        self.entry6 = tkinter.Entry(self.frame7, width=20)
        self.label6.pack(side="left")
        self.entry6.pack(side="left")

        self.label7 = tkinter.Label(self.frame8, text="Rate your genetic risk level (1-8):",
                                    font=("Helvetica bold", 10))
        self.entry7 = tkinter.Entry(self.frame8, width=20)
        self.label7.pack(side="left")
        self.entry7.pack(side="left")

        self.label8 = tkinter.Label(self.frame9, text="Rate your chronic lung disease level (1-8):",
                                    font=("Helvetica bold", 10))
        self.entry8 = tkinter.Entry(self.frame9, width=20)
        self.label8.pack(side="left")
        self.entry8.pack(side="left")

        self.label9 = tkinter.Label(self.frame10, text="Rate your balanced diet level (1-8):",
                                    font=("Helvetica bold", 10))
        self.entry9 = tkinter.Entry(self.frame10, width=20)
        self.label9.pack(side="left")
        self.entry9.pack(side="left")

        self.label10 = tkinter.Label(self.frame11, text="Rate your obesity level (1-8):", font=("Helvetica bold", 10))
        self.entry10 = tkinter.Entry(self.frame11, width=20)
        self.label10.pack(side="left")
        self.entry10.pack(side="left")

        self.label11 = tkinter.Label(self.frame12, text="Rate your smoking level (1-8):", font=("Helvetica bold", 10))
        self.entry11 = tkinter.Entry(self.frame12, width=20)
        self.label11.pack(side="left")
        self.entry11.pack(side="left")

        self.label12 = tkinter.Label(self.frame13, text="Rate your passive smoking level (1-8):",
                                     font=("Helvetica bold", 10))
        self.entry12 = tkinter.Entry(self.frame13, width=20)
        self.label12.pack(side="left")
        self.entry12.pack(side="left")

        # Next line
        self.label13 = tkinter.Label(self.frame2, text="Rate your chest pain level (1-8):", font=("Helvetica bold", 10))
        self.entry13 = tkinter.Entry(self.frame2, width=20)
        self.label13.pack(side="left", padx=(300, 0))
        self.entry13.pack(side="left")

        self.label14 = tkinter.Label(self.frame3, text="Rate your coughing of blood level (1-8):",
                                     font=("Helvetica bold", 10))
        self.entry14 = tkinter.Entry(self.frame3, width=20)
        self.label14.pack(side="left", padx=(82, 0))
        self.entry14.pack(side="left")

        self.label15 = tkinter.Label(self.frame4, text="Rate your fatigue level (1-8):", font=("Helvetica bold", 10))
        self.entry15 = tkinter.Entry(self.frame4, width=20)
        self.label15.pack(side="left", padx=(230, 0))
        self.entry15.pack(side="left")

        self.label16 = tkinter.Label(self.frame5, text="Rate your weight loss level (1-8):",
                                     font=("Helvetica bold", 10))
        self.entry16 = tkinter.Entry(self.frame5, width=20)
        self.label16.pack(side="left", padx=(180, 0))
        self.entry16.pack(side="left")

        self.label17 = tkinter.Label(self.frame6, text="Rate your shortness of breath level (1-8):",
                                     font=("Helvetica bold", 10))
        self.entry17 = tkinter.Entry(self.frame6, width=20)
        self.label17.pack(side="left", padx=(120, 0))
        self.entry17.pack(side="left")

        self.label18 = tkinter.Label(self.frame7, text="Rate your wheezing level (1-8):", font=("Helvetica bold", 10))
        self.entry18 = tkinter.Entry(self.frame7, width=20)
        self.label18.pack(side="left", padx=(100, 0))
        self.entry18.pack(side="left")

        self.label19 = tkinter.Label(self.frame8, text="Rate your swallowing difficulty level (1-8):",
                                     font=("Helvetica bold", 10))
        self.entry19 = tkinter.Entry(self.frame8, width=20)
        self.label19.pack(side="left", padx=(120, 0))
        self.entry19.pack(side="left")

        self.label20 = tkinter.Label(self.frame9, text="Rate your clubbing of finger nails level (1-8):",
                                     font=("Helvetica bold", 10))
        self.entry20 = tkinter.Entry(self.frame9, width=20)
        self.label20.pack(side="left", padx=(40, 0))
        self.entry20.pack(side="left")

        self.label21 = tkinter.Label(self.frame10, text="Rate your frequent cold level (1-8):",
                                     font=("Helvetica bold", 10))
        self.entry21 = tkinter.Entry(self.frame10, width=20)
        self.label21.pack(side="left", padx=(150, 0))
        self.entry21.pack(side="left")

        self.label22 = tkinter.Label(self.frame11, text="Rate your dry cough level (1-8):", font=("Helvetica bold", 10))
        self.entry22 = tkinter.Entry(self.frame11, width=20)
        self.label22.pack(side="left", padx=(220, 0))
        self.entry22.pack(side="left")

        self.label23 = tkinter.Label(self.frame12, text="Rate your snoring level (1-8):", font=("Helvetica bold", 10))
        self.entry23 = tkinter.Entry(self.frame12, width=20)
        self.label23.pack(side="left", padx=(220, 0))
        self.entry23.pack(side="left")

        self.button1 = tkinter.Button(self.frame14, text="Submit", padx=5, pady=5, command=self.evaluate)
        self.button1.pack(pady=20)

        # Pack frames
        self.frame1.configure(bg="blue")
        self.frame1.pack(ipady=20, fill="both")
        self.frame2.pack(padx=(150, 0), pady=(10, 0), anchor="w")
        self.frame3.pack(padx=(150, 0), pady=(10, 0), anchor="w")
        self.frame4.pack(padx=(150, 0), pady=(10, 0), anchor="w")
        self.frame5.pack(padx=(150, 0), pady=(10, 0), anchor="w")
        self.frame6.pack(padx=(150, 0), pady=(10, 0), anchor="w")
        self.frame7.pack(padx=(150, 0), pady=(10, 0), anchor="w")
        self.frame8.pack(padx=(150, 0), pady=(10, 0), anchor="w")
        self.frame9.pack(padx=(150, 0), pady=(10, 0), anchor="w")
        self.frame10.pack(padx=(150, 0), pady=(10, 0), anchor="w")
        self.frame11.pack(padx=(150, 0), pady=(10, 0), anchor="w")
        self.frame12.pack(padx=(150, 0), pady=(10, 0), anchor="w")
        self.frame13.pack(padx=(150, 0), pady=(10, 0), anchor="w")
        self.frame14.pack()

        tkinter.mainloop()

    def evaluate(self):
        # Get input
        Age = float(self.entry1.get())
        Gender = float(self.entry2.get())
        AirPollution = float(self.entry3.get())
        Alcohol_use = float(self.entry4.get())
        DustAllergy = float(self.entry5.get())
        OccuPationalHazards = float(self.entry6.get())
        GeneticRisk = float(self.entry7.get())
        ChronicLungDisease = float(self.entry8.get())
        BalancedDiet = float(self.entry9.get())
        Obesity = float(self.entry10.get())
        Smoking = float(self.entry11.get())
        PassiveSmoker = float(self.entry12.get())
        ChestPain = float(self.entry13.get())
        CoughingBlood = float(self.entry14.get())
        Fatigue = float(self.entry15.get())
        WeightLoss = float(self.entry16.get())
        ShortnessBreath = float(self.entry17.get())
        Wheezing = float(self.entry18.get())
        SwallowingDifficulty = float(self.entry19.get())
        ClubbingFingerNails = float(self.entry20.get())
        FrequentCold = float(self.entry21.get())
        DryCough = float(self.entry22.get())
        Snoring = float(self.entry23.get())

        # Store input
        patient_info = (
            Age, Gender, AirPollution, Alcohol_use, DustAllergy, OccuPationalHazards, GeneticRisk, ChronicLungDisease,
            BalancedDiet, Obesity, Smoking, PassiveSmoker, ChestPain, CoughingBlood, Fatigue, WeightLoss,
            ShortnessBreath,
            Wheezing, SwallowingDifficulty, ClubbingFingerNails, FrequentCold, DryCough, Snoring)

        # Use best model to make prediction
        LungCancer_prediction = lung_cancer_model_prediction.best_model.predict([patient_info])

        if LungCancer_prediction == [0]:
            low_risk = tkinter.Label(self.frame14, text="Low risk of lung cancer", font=("Helvetica bold", 20))
            low_risk.pack()
            # (9, 1, 2, 0, 3, 1, 2, 1, 2, 2, 1, 1, 3, 1, 1, 1, 2, 3, 0, 4, 1, 5, 1)


        elif LungCancer_prediction == [1]:
            medium_risk = tkinter.Label(self.frame14, text="Medium risk of lung cancer", font=("Helvetica bold", 20))
            medium_risk.pack()
            # (16, 0, 1, 0, 4, 2, 1, 2, 1, 3, 0, 3, 1, 3, 5, 6, 1, 4, 7, 0, 2, 1, 2)


        else:
            high_risk = tkinter.Label(self.frame14, text="Medium risk of lung cancer", font=("Helvetica bold", 20))
            high_risk.pack()
            # (6, 0, 5, 7, 6, 6, 5, 6, 6, 2, 7, 6, 8, 5, 4, 1, 4, 1, 2, 1, 0, 6, 5)


my_GUI = LungCancer_GUI()
