## Access Instructions for QSIDE Human Trafficking's Data

#### Note: 
This repository contains both an Excel Workbook (`.xlsx` extension) formatted spreadsheet containing all of our independent research, as well as some exploratory and experimental Jupyter notebooks written in Python. A Python environment is not needed if you only want to view the data bibliography.

---


### 1. Cloning Data from GitHub
The following command can be used to access and clone the repository to your local environment.

`git clone https://github.com/jacknuge28/QSIDE_HumanTrafficking`


### 2. Accessing the Data Bibliography
In the top level of the QSIDE_HumanTrafficking repository, the data bibliography in a tabled format is available within `DataBibliography.xlsx`. 

<!-- #region -->
---

**<p style="text-align: center;">The following requires access to a Python IDE.</p>**

### 3. Exploratory Notebooks
The notebooks available in the *Figures* subdirectory contain our initial exploratory work in Jupyter notebooks.

To set up the required environment for these notebooks, use the following commands:

`conda env create --prefix ./envs --file environment.yml`<br>
`conda activate ./envs`

# NOTE: WIP

- **001_Image_Reproducibility.ipynb** : Contains graphics breaking down the tagging-in-place system used within our data bibliography
- **002_MI_school_poverty.ipynb** : A deeper dive into one facet of the broader human trafficking problem, involves analysis of youth poverty rates by county in Michigan from the SAIPE School District Estimates for 2021.



The *Figure_Details* subdirectory within *Figures* contains more detailed notes about figure generation, if detail was provided.
<!-- #endregion -->
