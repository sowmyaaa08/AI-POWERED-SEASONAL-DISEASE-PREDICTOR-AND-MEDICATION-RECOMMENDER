DISEASE_DATA = {
    "Flu": {
        "symptoms": ["Fever", "Cough", "Sore throat", "Body pain", "Headache", "Fatigue"],
        "medicines": ["Paracetamol", "Oseltamivir"],
        "ayurvedic": ["Ginger tea", "Tulsi decoction", "Turmeric milk"],
        "diet": ["Warm fluids", "Soup", "Easy-to-digest food"]
    },
    "Common Cold": {
        "symptoms": ["Runny nose", "Sneezing", "Cough", "Sore throat", "Headache"],
        "medicines": ["Antihistamines", "Nasal sprays"],
        "ayurvedic": ["Honey and ginger juice", "Steaming with eucalyptus oil"],
        "diet": ["Hot herbal teas", "Warm water", "Vitamin C rich fruits"]
    },
    "Dengue": {
        "symptoms": ["High fever", "Headache", "Joint pain", "Skin rash", "Nausea"],
        "medicines": ["Acetaminophen (Avoid Ibuprofen/Aspirin)"],
        "ayurvedic": ["Papaya leaf juice", "Giloy juice", "Neem leaves"],
        "diet": ["Hydrating fluids", "Coconut water", "Fresh fruit juices"]
    },
    "Malaria": {
        "symptoms": ["Fever", "Chills", "Sweating", "Headache", "Nausea"],
        "medicines": ["Chloroquine", "Artemisinin-based combination therapy (ACT)"],
        "ayurvedic": ["Sudarshan Ghan Vati", "Kiratatikta decoction"],
        "diet": ["Easily digestible food", "High calorie, high protein diet"]
    },
    "Typhoid": {
        "symptoms": ["High fever", "Weakness", "Abdominal pain", "Headache", "Loss of appetite"],
        "medicines": ["Ciprofloxacin", "Azithromycin"],
        "ayurvedic": ["Khubani (Dried apricots)", "Musta (Cyperus rotundus)"],
        "diet": ["High-calorie diet", "Boiled water", "Semi-solid foods like porridge"]
    },
    "Chikungunya": {
        "symptoms": ["Fever", "Joint pain", "Muscle pain", "Headache", "Skin rash"],
        "medicines": ["NSAIDs (Naproxen, Ibuprofen)"],
        "ayurvedic": ["Ashwagandha", "Shallaki"],
        "diet": ["Anti-inflammatory foods", "Omega-3 rich foods", "Hydration"]
    },
    "COVID-19": {
        "symptoms": ["Fever", "Cough", "Breathing difficulty", "Loss of smell", "Fatigue"],
        "medicines": ["Remdesivir (for severe cases)", "Paxlovid"],
        "ayurvedic": ["Chyawanprash", "Ayush Kwath (Kadha)"],
        "diet": ["Protein-rich diet", "Fresh fruits", "Warm water"]
    },
    "Asthma": {
        "symptoms": ["Shortness of breath", "Wheezing", "Cough", "Chest tightness"],
        "medicines": ["Salbutamol inhaler", "Corticosteroids"],
        "ayurvedic": ["Kantakari", "Vasa"],
        "diet": ["Avoid cold drinks", "Magnesium-rich foods", "Ginger"]
    },
    "Bronchitis": {
        "symptoms": ["Cough", "Mucus production", "Fatigue", "Chest discomfort"],
        "medicines": ["Guaifenesin", "Albuterol"],
        "ayurvedic": ["Tulsi", "Licorice root"],
        "diet": ["Hot soups", "Hydration", "Garlic"]
    },
    "Pneumonia": {
        "symptoms": ["Fever", "Cough", "Breathing difficulty", "Chest pain", "Fatigue"],
        "medicines": ["Amoxicillin", "Azithromycin"],
        "ayurvedic": ["Dashamoola", "Triphala"],
        "diet": ["Warm liquids", "High protein", "Vitamin C rich food"]
    },
    "Tuberculosis": {
        "symptoms": ["Chronic cough", "Weight loss", "Fever", "Night sweats"],
        "medicines": ["Isoniazid", "Rifampin", "Ethambutol"],
        "ayurvedic": ["Ashwagandha", "Guduchi"],
        "diet": ["High calorie and high protein diet", "Peanuts", "Green leafy vegetables"]
    },
    "Allergy": {
        "symptoms": ["Sneezing", "Runny nose", "Itchy eyes", "Skin rash"],
        "medicines": ["Loratadine", "Cetirizine"],
        "ayurvedic": ["Haridra Khanda", "Triphala"],
        "diet": ["Avoid allergens", "Quercetin rich foods like apples"]
    },
    "Food Poisoning": {
        "symptoms": ["Nausea", "Vomiting", "Diarrhea", "Abdominal pain", "Fever"],
        "medicines": ["Bismuth subsalicylate", "Loperamide"],
        "ayurvedic": ["Jeerakaarishtam", "Musta"],
        "diet": ["BRAT diet (Bananas, Rice, Applesauce, Toast)", "Electrolytes"]
    },
    "Gastroenteritis": {
        "symptoms": ["Diarrhea", "Vomiting", "Stomach pain", "Fever"],
        "medicines": ["Oral rehydration salts (ORS)", "Zinc supplements"],
        "ayurvedic": ["Bilwadi Lehyam", "Kutajarishta"],
        "diet": ["Clear liquids", "Bland foods", "Probiotics like yogurt"]
    },
    "Migraine": {
        "symptoms": ["Severe headache", "Nausea", "Sensitivity to light", "Blurred vision"],
        "medicines": ["Sumatriptan", "Ibuprofen"],
        "ayurvedic": ["Brahmi", "Peppermint oil application"],
        "diet": ["Magnesium-rich foods", "Hydration", "Avoid caffeine/chocolate triggers"]
    },
    "Sinusitis": {
        "symptoms": ["Headache", "Facial pain", "Runny nose", "Nasal congestion"],
        "medicines": ["Pseudoephedrine", "Fluticasone"],
        "ayurvedic": ["Nasya therapy with Anu taila", "Steam inhalation"],
        "diet": ["Spicy food (to clear nasal passage)", "Hot soup", "Avoid dairy if it increases mucus"]
    },
    "Chickenpox": {
        "symptoms": ["Fever", "Skin rash", "Itchy blisters", "Fatigue"],
        "medicines": ["Acyclovir", "Calamine lotion"],
        "ayurvedic": ["Neem leaf paste application", "Guduchi"],
        "diet": ["Bland diet", "Cooling foods", "Fruit juices"]
    },
    "Measles": {
        "symptoms": ["Fever", "Rash", "Runny nose", "Cough"],
        "medicines": ["Vitamin A supplements", "Acetaminophen"],
        "ayurvedic": ["Turmeric and neem decoction", "Guduchi"],
        "diet": ["High Vitamin A foods", "Hydration", "Easily digestible food"]
    },
    "Mumps": {
        "symptoms": ["Swollen glands", "Fever", "Headache", "Muscle pain"],
        "medicines": ["Ibuprofen", "Warm/cold packs for glands"],
        "ayurvedic": ["Haridra (Turmeric) paste on swelling", "Triphala"],
        "diet": ["Soft foods", "Avoid acidic drinks", "Soup"]
    },
    "Hepatitis A": {
        "symptoms": ["Fatigue", "Nausea", "Abdominal pain", "Yellow skin"],
        "medicines": ["Supportive care", "Avoid alcohol/medications processed by liver"],
        "ayurvedic": ["Bhumyamalaki", "Katuki"],
        "diet": ["Low fat diet", "Small frequent meals", "Sugarcane juice"]
    },
    "Hepatitis B": {
        "symptoms": ["Fever", "Fatigue", "Nausea", "Joint pain"],
        "medicines": ["Tenofovir", "Entecavir"],
        "ayurvedic": ["Guduchi", "Punarnava"],
        "diet": ["Liver-friendly diet", "Fresh fruits", "Avoid alcohol"]
    },
    "Hepatitis C": {
        "symptoms": ["Fatigue", "Loss of appetite", "Nausea", "Abdominal pain"],
        "medicines": ["Sofosbuvir", "Velpatasvir"],
        "ayurvedic": ["Amla", "Kalmegh"],
        "diet": ["Balanced diet", "Avoid alcohol", "Low salt if liver damage"]
    },
    "Diabetes": {
        "symptoms": ["Frequent urination", "Excess thirst", "Weight loss", "Fatigue"],
        "medicines": ["Metformin", "Insulin"],
        "ayurvedic": ["Nisha-Amalaki", "Gymnema sylvestre (Gudmar)"],
        "diet": ["Low glycemic index foods", "High fiber", "Bitter gourd juice"]
    },
    "Hypertension": {
        "symptoms": ["Headache", "Dizziness", "Nosebleeds"],
        "medicines": ["Amlodipine", "Lisinopril"],
        "ayurvedic": ["Sarpagandha", "Arjuna"],
        "diet": ["Low sodium (DASH diet)", "Potassium-rich foods", "Avoid alcohol"]
    },
    "Anemia": {
        "symptoms": ["Fatigue", "Weakness", "Pale skin", "Dizziness"],
        "medicines": ["Iron supplements", "Vitamin B12 supplements"],
        "ayurvedic": ["Punarnava Mandur", "Dhatri Lauha"],
        "diet": ["Iron-rich foods (Spinach, Pomegranate)", "Vitamin C (for absorption)"]
    },
    "Arthritis": {
        "symptoms": ["Joint pain", "Swelling", "Stiffness", "Reduced movement"],
        "medicines": ["Methotrexate", "Naproxen"],
        "ayurvedic": ["Shallaki", "Guggulu"],
        "diet": ["Omega-3 rich foods", "Turmeric", "Avoid inflammatory foods"]
    },
    "Osteoporosis": {
        "symptoms": ["Back pain", "Fractures", "Loss of height"],
        "medicines": ["Alendronate", "Calcium/Vitamin D supplements"],
        "ayurvedic": ["Ashwagandha", "Lakshadi Guggulu"],
        "diet": ["Calcium-rich foods (Dairy, Ragi)", "Vitamin D (Sunlight, Eggs)"]
    },
    "Kidney Stones": {
        "symptoms": ["Severe back pain", "Nausea", "Vomiting", "Blood in urine"],
        "medicines": ["Tamsulosin", "Pain relievers"],
        "ayurvedic": ["Varuna", "Pashanabheda"],
        "diet": ["Increase water intake", "Avoid oxalates (Spinach, Beetroot)"]
    },
    "Urinary Infection": {
        "symptoms": ["Burning urination", "Frequent urination", "Fever"],
        "medicines": ["Nitrofurantoin", "Ciprofloxacin"],
        "ayurvedic": ["Gokshura", "Chandraprabha Vati"],
        "diet": ["Cranberry juice", "High water intake", "Avoid caffeine"]
    },
    "Appendicitis": {
        "symptoms": ["Abdominal pain", "Nausea", "Vomiting", "Fever"],
        "medicines": ["Surgery (Appendectomy)", "Antibiotics"],
        "ayurvedic": ["Supportive only - Consult Surgeon", "Aloe Vera juice (post-op)"],
        "diet": ["Liquid diet initially", "High fiber (after recovery)"]
    },
    "Gallstones": {
        "symptoms": ["Abdominal pain", "Nausea", "Vomiting", "Indigestion"],
        "medicines": ["Ursodeoxycholic acid", "Surgery (Cholecystectomy)"],
        "ayurvedic": ["Kalmegh", "Katuki"],
        "diet": ["Low fat diet", "High fiber", "Avoid greasy foods"]
    },
    "Pancreatitis": {
        "symptoms": ["Severe abdominal pain", "Nausea", "Vomiting", "Fever"],
        "medicines": ["IV Fluids", "Pain management"],
        "ayurvedic": ["Supportive - Consult Specialist", "Amla juice"],
        "diet": ["Low fat diet", "Small meals", "Avoid alcohol"]
    },
    "Peptic Ulcer": {
        "symptoms": ["Stomach pain", "Bloating", "Nausea", "Heartburn"],
        "medicines": ["Omeprazole", "Clarithromycin"],
        "ayurvedic": ["Shatavari", "Yashtimadhu (Licorice)"],
        "diet": ["Avoid spicy foods", "Small frequent meals", "Cold milk"]
    },
    "Acid Reflux": {
        "symptoms": ["Heartburn", "Chest pain", "Nausea", "Sore throat"],
        "medicines": ["Antacids", "Pantoprazole"],
        "ayurvedic": ["Amla juice", "Avipattikar Churna"],
        "diet": ["Avoid caffeine/spicy foods", "Eat 2-3 hours before bed"]
    },
    "Constipation": {
        "symptoms": ["Hard stools", "Abdominal discomfort", "Bloating"],
        "medicines": ["Bisacodyl", "Psyllium husk"],
        "ayurvedic": ["Triphala Churna", "Isabgol"],
        "diet": ["High fiber diet", "Plenty of water", "Papaya"]
    },
    "Diarrhea": {
        "symptoms": ["Loose stools", "Dehydration", "Abdominal pain"],
        "medicines": ["Loperamide", "ORS"],
        "ayurvedic": ["Kutaja", "Bilwa (Bael)"],
        "diet": ["BRAT diet", "Hydration", "Yogurt"]
    },
    "Irritable Bowel Syndrome": {
        "symptoms": ["Abdominal pain", "Bloating", "Diarrhea"],
        "medicines": ["Dicyclomine", "Linaclotide"],
        "ayurvedic": ["Takra (Buttermilk) with cumin", "Ginger"],
        "diet": ["Low FODMAP diet", "Probiotics", "Avoid triggers"]
    },
    "Celiac Disease": {
        "symptoms": ["Diarrhea", "Weight loss", "Bloating"],
        "medicines": ["Gluten-free diet (Main treatment)"],
        "ayurvedic": ["Supportive - Digestive herbs like Trikatu"],
        "diet": ["Strict Gluten-free diet", "Quinoa", "Rice"]
    },
    "Crohn's Disease": {
        "symptoms": ["Abdominal pain", "Diarrhea", "Weight loss"],
        "medicines": ["Infliximab", "Prednisone"],
        "ayurvedic": ["Guduchi", "Musta"],
        "diet": ["Low residue diet during flares", "Hydration"]
    },
    "Ulcerative Colitis": {
        "symptoms": ["Abdominal pain", "Bloody diarrhea", "Fatigue"],
        "medicines": ["Mesalamine", "Azathioprine"],
        "ayurvedic": ["Kutajarishta", "Bilwadi Lehyam"],
        "diet": ["Soft, bland diet", "Avoid dairy and high fiber during flare"]
    },
    "Parkinson's Disease": {
        "symptoms": ["Tremor", "Slow movement", "Muscle stiffness"],
        "medicines": ["Levodopa", "Carbidopa"],
        "ayurvedic": ["Kapikachhu (Mucuna pruriens)", "Ashwagandha"],
        "diet": ["High fiber", "Hydration", "Balanced nutrients"]
    },
    "Alzheimer's Disease": {
        "symptoms": ["Memory loss", "Confusion", "Behavior changes"],
        "medicines": ["Donepezil", "Memantine"],
        "ayurvedic": ["Brahmi", "Shankhapushpi"],
        "diet": ["Mediterranean diet", "Omega-3 rich foods", "Antioxidants"]
    },
    "Epilepsy": {
        "symptoms": ["Seizures", "Confusion", "Loss of awareness"],
        "medicines": ["Valproate", "Levetiracetam"],
        "ayurvedic": ["Brahmi", "Vacha"],
        "diet": ["Ketogenic diet (sometimes recommended)", "Avoid alcohol"]
    },
    "Stroke": {
        "symptoms": ["Weakness", "Speech difficulty", "Vision problems"],
        "medicines": ["Alteplase (within hours)", "Aspirin"],
        "ayurvedic": ["Arjuna", "Ashwagandha (for recovery)"],
        "diet": ["Low salt, low fat", "Heart-healthy diet"]
    },
    "Multiple Sclerosis": {
        "symptoms": ["Vision problems", "Muscle weakness", "Fatigue"],
        "medicines": ["Interferon beta", "Glatiramer acetate"],
        "ayurvedic": ["Ashwagandha", "Guduchi"],
        "diet": ["Anti-inflammatory diet", "Vitamin D rich foods"]
    },
    "Depression": {
        "symptoms": ["Sadness", "Fatigue", "Loss of interest"],
        "medicines": ["Sertraline", "Fluoxetine"],
        "ayurvedic": ["Brahmi", "Ashwagandha"],
        "diet": ["Foods rich in B vitamins", "Magnesium", "Omega-3"]
    },
    "Anxiety": {
        "symptoms": ["Restlessness", "Rapid heartbeat", "Sweating"],
        "medicines": ["Alprazolam", "Escitalopram"],
        "ayurvedic": ["Jatamansi", "Shankhapushpi"],
        "diet": ["Avoid caffeine", "Chamomile tea", "Magnesium rich foods"]
    },
    "Insomnia": {
        "symptoms": ["Difficulty sleeping", "Fatigue", "Irritability"],
        "medicines": ["Zolpidem", "Melatonin"],
        "ayurvedic": ["Ashwagandha at night", "Tagara"],
        "diet": ["Warm milk", "Almonds", "Avoid heavy meals at night"]
    },
    "Obesity": {
        "symptoms": ["Excess body weight", "Fatigue", "Breathing difficulty"],
        "medicines": ["Orlistat", "Phentermine"],
        "ayurvedic": ["Guggulu", "Triphala", "Honey with warm water"],
        "diet": ["Calorie deficit", "High fiber", "Low carb"]
    },
    "Heat Stroke": {
        "symptoms": ["High body temperature", "Dizziness", "Nausea"],
        "medicines": ["Cooling measures", "IV fluids"],
        "ayurvedic": ["Pandan/Vetiver water", "Amalaki"],
        "diet": ["Buttermilk", "Coconut water", "Cooling foods"]
    },
    "Heat Exhaustion": {
        "symptoms": ["Sweating", "Weakness", "Dizziness"],
        "medicines": ["Electrolytes", "Rest in cool place"],
        "ayurvedic": ["Gulab (Rose) water", "Amla juice"],
        "diet": ["Hydrating fluids", "Watermelon", "Cucumber"]
    },
    "Hypothermia": {
        "symptoms": ["Shivering", "Confusion", "Slow breathing"],
        "medicines": ["Warming measures"],
        "ayurvedic": ["Ginger tea", "Cinnamon", "Warm soup"],
        "diet": ["Warm high-calorie food", "Hot drinks"]
    },
    "Lyme Disease": {
        "symptoms": ["Fever", "Rash", "Joint pain"],
        "medicines": ["Doxycycline", "Amoxicillin"],
        "ayurvedic": ["Guduchi", "Neem"],
        "diet": ["Anti-inflammatory diet", "Immune boosting foods"]
    },
    "Rabies": {
        "symptoms": ["Fever", "Hydrophobia", "Confusion"],
        "medicines": ["Rabies Vaccine", "HRIG"],
        "ayurvedic": ["None - Immediate Medical Attention Required"],
        "diet": ["None - Critical Care"]
    },
    "Tetanus": {
        "symptoms": ["Muscle stiffness", "Jaw locking", "Spasms"],
        "medicines": ["Tetanus Antitoxin", "Metronidazole"],
        "ayurvedic": ["Supportive care - Immediate Medical Attention"],
        "diet": ["Liquid diet if jaw locked"]
    },
    "Polio": {
        "symptoms": ["Muscle weakness", "Paralysis", "Fever"],
        "medicines": ["Supportive care", "Physical therapy"],
        "ayurvedic": ["Bala (Sida cordifolia)", "Ashwagandha"],
        "diet": ["Nutritious balanced diet"]
    },
    "Leprosy": {
        "symptoms": ["Skin lesions", "Numbness", "Muscle weakness"],
        "medicines": ["Dapsone", "Rifampicin", "Clofazimine"],
        "ayurvedic": ["Manjistha", "Khadira"],
        "diet": ["Healthy balanced diet"]
    },
    "Scabies": {
        "symptoms": ["Itching", "Skin rash", "Red bumps"],
        "medicines": ["Permethrin cream", "Ivermectin"],
        "ayurvedic": ["Neem oil", "Turmeric paste"],
        "diet": ["None specific"]
    },
    "Ringworm": {
        "symptoms": ["Red rash", "Itching", "Circular patches"],
        "medicines": ["Clotrimazole", "Terbinafine"],
        "ayurvedic": ["Neem paste", "Garlic extract application"],
        "diet": ["Avoid sugar and yeast-rich foods"]
    },
    "Psoriasis": {
        "symptoms": ["Red patches", "Scaly skin", "Itching"],
        "medicines": ["Topical Steroids", "Methotrexate"],
        "ayurvedic": ["Nimba (Neem)", "Patola"],
        "diet": ["Anti-inflammatory diet", "Avoid alcohol/red meat"]
    },
    "Eczema": {
        "symptoms": ["Dry skin", "Itching", "Rash"],
        "medicines": ["Hydrocortisone cream", "Antihistamines"],
        "ayurvedic": ["Coconut oil with Camphor", "Aloe Vera"],
        "diet": ["Identify and avoid food triggers"]
    },
    "Acne": {
        "symptoms": ["Pimples", "Redness", "Skin inflammation"],
        "medicines": ["Benzoyl peroxide", "Salicylic acid"],
        "ayurvedic": ["Neem", "Aloe Vera", "Manjistha"],
        "diet": ["Low glycemic diet", "Avoid dairy/sugar if triggering"]
    },
    "Glaucoma": {
        "symptoms": ["Eye pain", "Blurred vision", "Headache"],
        "medicines": ["Latanoprost", "Timolol"],
        "ayurvedic": ["Triphala Ghrita", "Punarnava"],
        "diet": ["Leafy greens", "Antioxidants"]
    },
    "Cataract": {
        "symptoms": ["Blurred vision", "Sensitivity to light"],
        "medicines": ["Surgery (Phacoemulsification)"],
        "ayurvedic": ["Triphala eye wash", "Maha Triphala Ghrita"],
        "diet": ["Vitamin C and E rich foods"]
    },
    "Conjunctivitis": {
        "symptoms": ["Red eyes", "Itching", "Tearing"],
        "medicines": ["Antibiotic eye drops", "Artificial tears"],
        "ayurvedic": ["Rose water drops", "Triphala wash"],
        "diet": ["None specific"]
    },
    "Otitis": {
        "symptoms": ["Ear pain", "Fever", "Hearing loss"],
        "medicines": ["Amoxicillin", "Pain relievers"],
        "ayurvedic": ["Bilwa taila", "Kshara taila ear drops"],
        "diet": ["Avoid cold foods"]
    },
    "Tonsillitis": {
        "symptoms": ["Sore throat", "Fever", "Swollen tonsils"],
        "medicines": ["Penicillin", "Ibuprofen"],
        "ayurvedic": ["Turmeric and salt gargle", "Khadiradi Vati"],
        "diet": ["Soft foods", "Warm liquids"]
    },
    "Laryngitis": {
        "symptoms": ["Hoarseness", "Sore throat", "Cough"],
        "medicines": ["Rest voice", "Hydration"],
        "ayurvedic": ["Yashtimadhu", "Ginger honey juice"],
        "diet": ["Avoid spicy and cold foods"]
    },
    "Pharyngitis": {
        "symptoms": ["Sore throat", "Fever", "Swollen glands"],
        "medicines": ["Acetaminophen", "Gargling"],
        "ayurvedic": ["Tulsi decoction", "Licorice"],
        "diet": ["Warm soups", "Herbal tea"]
    },
    "Diphtheria": {
        "symptoms": ["Sore throat", "Fever", "Weakness"],
        "medicines": ["Diphtheria Antitoxin", "Erythromycin"],
        "ayurvedic": ["Supportive - Consult Hospital"],
        "diet": ["Liquid diet"]
    },
    "Whooping Cough": {
        "symptoms": ["Severe cough", "Runny nose", "Fever"],
        "medicines": ["Azithromycin", "Cough suppressants"],
        "ayurvedic": ["Vasa", "Kantakari"],
        "diet": ["Small frequent meals", "Hydration"]
    },
    "Influenza": {
        "symptoms": ["Fever", "Body pain", "Cough", "Fatigue"],
        "medicines": ["Oseltamivir", "Paracetamol"],
        "ayurvedic": ["Amritarishta", "Guduchi"],
        "diet": ["Hydration", "Vitamin C", "Warm food"]
    },
    "Norovirus": {
        "symptoms": ["Vomiting", "Diarrhea", "Stomach pain"],
        "medicines": ["ORS", "Anti-emetics"],
        "ayurvedic": ["Musta", "Bilwa"],
        "diet": ["Clear liquids", "Bland diet"]
    },
    "Rotavirus": {
        "symptoms": ["Diarrhea", "Vomiting", "Fever"],
        "medicines": ["ORS", "Zinc supplements"],
        "ayurvedic": ["Kutajarishta", "Bilwadi Lehyam"],
        "diet": ["Hydration", "Bland diet"]
    },
    "Zika Virus": {
        "symptoms": ["Fever", "Rash", "Joint pain"],
        "medicines": ["Rest", "Hydration", "Acetaminophen"],
        "ayurvedic": ["Guduchi", "Tulsi"],
        "diet": ["Hydration", "Fresh fruits"]
    },
    "Yellow Fever": {
        "symptoms": ["Fever", "Chills", "Headache"],
        "medicines": ["Supportive care", "Fluid replacement"],
        "ayurvedic": ["Bhumyamalaki", "Katuki"],
        "diet": ["High fluid intake", "Easy to digest food"]
    },
    "West Nile Virus": {
        "symptoms": ["Fever", "Headache", "Body aches"],
        "medicines": ["Pain relievers", "Supportive care"],
        "ayurvedic": ["Ashwagandha", "Guduchi"],
        "diet": ["Balanced diet", "Rest"]
    },
    "Ebola": {
        "symptoms": ["Fever", "Bleeding", "Vomiting"],
        "medicines": ["Inmazeb", "Ebanga"],
        "ayurvedic": ["None - Critical Hospitalization"],
        "diet": ["IV fluids and nutrition"]
    },
    "Marburg Virus": {
        "symptoms": ["Fever", "Severe headache", "Muscle pain"],
        "medicines": ["Supportive care", "Rehydration"],
        "ayurvedic": ["None - Critical Hospitalization"],
        "diet": ["IV fluids"]
    },
    "Plague": {
        "symptoms": ["Fever", "Chills", "Swollen lymph nodes"],
        "medicines": ["Gentamicin", "Doxycycline"],
        "ayurvedic": ["None - Immediate Medical Attention"],
        "diet": ["High protein and fluids during recovery"]
    },
    "Cholera": {
        "symptoms": ["Severe diarrhea", "Dehydration", "Vomiting"],
        "medicines": ["Doxycycline", "Azithromycin", "ORS"],
        "ayurvedic": ["Kutajarishta", "Bilwadi Lehyam"],
        "diet": ["Heavy hydration (ORS)", "Bland liquid diet"]
    },
    "Botulism": {
        "symptoms": ["Muscle weakness", "Blurred vision", "Difficulty swallowing"],
        "medicines": ["Antitoxin"],
        "ayurvedic": ["None - Critical Care Required"],
        "diet": ["Tube feeding if swallowing is impossible"]
    },
    "Anthrax": {
        "symptoms": ["Fever", "Chest pain", "Cough"],
        "medicines": ["Ciprofloxacin", "Doxycycline"],
        "ayurvedic": ["None - Hospital Care Required"],
        "diet": ["Supportive nutrition"]
    },
    "Leptospirosis": {
        "symptoms": ["Fever", "Headache", "Muscle pain"],
        "medicines": ["Doxycycline", "Penicillin"],
        "ayurvedic": ["Punarnava", "Guduchi"],
        "diet": ["Balanced diet", "Hydration"]
    },
    "Brucellosis": {
        "symptoms": ["Fever", "Sweating", "Joint pain"],
        "medicines": ["Doxycycline", "Rifampin"],
        "ayurvedic": ["Ashwagandha", "Shallaki"],
        "diet": ["High calorie diet", "Rest"]
    },
    "Q Fever": {
        "symptoms": ["Fever", "Headache", "Fatigue"],
        "medicines": ["Doxycycline"],
        "ayurvedic": ["Guduchi", "Amalaki"],
        "diet": ["Balanced diet", "Hydration"]
    },
    "Tularemia": {
        "symptoms": ["Fever", "Skin ulcers", "Swollen glands"],
        "medicines": ["Streptomycin", "Gentamicin"],
        "ayurvedic": ["Manjistha", "Guduchi"],
        "diet": ["High protein diet"]
    },
    "Hantavirus": {
        "symptoms": ["Fever", "Muscle aches", "Breathing problems"],
        "medicines": ["Supportive care", "Oxygen therapy"],
        "ayurvedic": ["Vasa", "Kantakari"],
        "diet": ["Nutritious liquids"]
    },
    "SARS": {
        "symptoms": ["Fever", "Cough", "Breathing difficulty"],
        "medicines": ["Antivirals", "Corticosteroids"],
        "ayurvedic": ["Ayush Kwath", "Chyawanprash"],
        "diet": ["High protein", "Warm liquids"]
    },
    "MERS": {
        "symptoms": ["Fever", "Cough", "Shortness of breath"],
        "medicines": ["Supportive care", "Oxygen therapy"],
        "ayurvedic": ["Vasa", "Dashamoola"],
        "diet": ["Nutritious soft foods", "Hydration"]
    },
    "Swine Flu": {
        "symptoms": ["Fever", "Cough", "Sore throat"],
        "medicines": ["Oseltamivir"],
        "ayurvedic": ["Tulsi", "Ginger", "Guduchi"],
        "diet": ["Warm liquids", "Vitamin C rich food"]
    },
    "Bird Flu": {
        "symptoms": ["Fever", "Cough", "Muscle pain"],
        "medicines": ["Oseltamivir", "Zanamivir"],
        "ayurvedic": ["Amritarishta", "Guduchi"],
        "diet": ["Hydration", "Balanced nutrition"]
    },
    "Seasonal Allergy": {
        "symptoms": ["Sneezing", "Runny nose", "Itchy eyes"],
        "medicines": ["Cetirizine", "Flonase"],
        "ayurvedic": ["Haridra Khanda", "Anu taila Nasya"],
        "diet": ["Avoid dairy and cold foods"]
    },
    "Motion Sickness": {
        "symptoms": ["Nausea", "Dizziness", "Vomiting"],
        "medicines": ["Dimenhydrinate", "Scopolamine patch"],
        "ayurvedic": ["Ginger chew", "Elaichi (Cardamom)"],
        "diet": ["Light snacks", "Avoid heavy meals before travel"]
    },
    "Altitude Sickness": {
        "symptoms": ["Headache", "Nausea", "Dizziness"],
        "medicines": ["Acetazolamide", "Oxygen"],
        "ayurvedic": ["Ginger", "Garlic"],
        "diet": ["High carb diet", "Hydration", "Avoid alcohol"]
    },
    "Dehydration": {
        "symptoms": ["Thirst", "Dizziness", "Fatigue"],
        "medicines": ["ORS", "IV fluids"],
        "ayurvedic": ["Coconut water", "Amla juice"],
        "diet": ["Hydrating foods like watermelon, cucumber", "Water"]
    }
}

ALL_SYMPTOMS = sorted(list(set([s for d in DISEASE_DATA.values() for s in d["symptoms"]])))
