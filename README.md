# Author 👥 : Adil Rasheed
# Crop Prediction 🌱
# Introduction 📝
Accurate and timely estimation of crop yield at a small scale is of great significance to food security and harvest management. Recent studies have proven remote sensing is an efficient method for yield estimation and machine learning, especially deep learning, can infer a good prediction by integrating multi-source datasets like satellite data, climate data, soil data, and so on. However, there are some bottleneck challenges to improve accuracy. First, the popular remote sensing data used for yield prediction fall into two major groups, time-series data, and constant data. Surprisingly little attention has been devoted to deep learning networks that can integrate the two kinds of data effectively; second, both temporal and spatial features play a role in affecting the yields. This paper proposed a novel multi-level deep learning (MLDL) model coupling RNN and CNN to extract both spatial and temporal features. The inputs include both time-series remote sensing data and soil property data and the model outputs yield.

The dataset consists of 8 variables:
- **N:** Nitrogen content in the soil.
- **P:** Phosphorus content in the soil.
- **K:** Potassium content in the soil.
- **Temperature:** Average temperature in Celsius during the crop growth period.
- **Humidity:** Average relative humidity during the crop growth period.
- **pH:** Soil pH level, indicating acidity or alkalinity.
- **Rainfall:** Total rainfall in mm during the crop growth period.
- **Label:** The type of crop being grown.
