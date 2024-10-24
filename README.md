# nOEN. n-Order Ecological Network

![Logo](Logo/Banner.png)
<br>*Contributors: Eloi Martinez-Rabert*

n-Order Ecological Network (nOEN) is a statistical platform to identify the ecological interactions (pairwise and higher-order) that control the community assembly. This platform is based on the multivariate iota coefficient (ι<sub>N</sub>), a new non-parametric association measure between two or more variables based on the concept of _paired orthants_[^1]. 

For **pairwise interactions** (2 joint variables), ι<sub>2</sub> corresponds to conventional Kendall's Tau (τ)[^2]. ι<sub>2</sub> (and Kendall's τ) ranges from -1 to +1. A value of -1 indicates that one dataset ranking is the reverse of the other (i.e., negative correlation), whereas a value of +1 indicates that the two rankings of datasets are the same (i.e., positive correlation). A value of 0 indicates no correlation between datasets. The ecological interpretation of ι<sub>2</sub> coefficients depend on the type of ecological interaction:

<p align="center">
    <img src="https://github.com/soundslikealloy/nOEN-py/assets/81569132/aa09e542-12b1-4112-8ebc-d54f732d241c">
</p>

For **higher-order interactions** (>2 joint variables), ι<sub>N>2</sub> also ranges from -1 to +1. A value of +1 indicates that the _N_ ranking of datasets follows the particular tendency (represented with +/↑ and -/↓), whereas a value of -1 indicatest that the _N_ ranking of datasets follows another tendency entirely. A value of 0 indicates no correlation among datasets. A unique ι<sub>N</sub> coefficient is associated to a specific data trend, that is, a higher-order interaction. For example, for the dataset in template file (`/Data/Template/template.xlsx`) and example file (`/Data/example.xlsx`):

<p align="center">
    <img src="https://github.com/soundslikealloy/nOEN-py/assets/81569132/bfda81a3-9329-482f-8394-ab95e55e1816">
</p>

____________________________

## Before having fun...
**:warning: To open the links in a new tab: right click on the link + "Open link in new tab".**

### :gear: Anaconda Python installation
This code is built up in Python. To execute this Python scripts is recommended the installation of **Anaconda**. **Anaconda Python** is a free, open-source platform that allows to write and execute code in the programming language Python ([Python Tutorial](https://docs.python.org/3/tutorial/index.html)). This platform simplifies package installation, managment and development, and alos comes with a large number of libraries/packages that can be you for your projects. To install **Anaconda**, just head to the [Anaconda Documentation website](https://docs.anaconda.com/free/anaconda/install/index.html) and follow the instructions to download teh installer for your operating system.

### Anaconda Navigator
Anaconda Navigator is a desktop graphical user interface that allows you to launch applications and efficiently manage conda packages, environments, and channels without using command-line commands. For more info, click [here](https://docs.anaconda.com/free/navigator/).

### Anaconda Prompt or Terminal
Anaconda Prompt is a command line interface with Anaconda Distribution. Terminal is a command line interface that comes with macOS and Linux. To open it in **Windows**: Click Start, search for _"Anaconda Prompt"_ and click to open. In **macOS**: use Cmd+Space to open Spotlight Search and type _"Navigator"_ to open the program. In **Linux-CentOS**: open Applications > System Tools > Terminal.

### Spyder
Spyder is a Python development environment with many features for working with Python code, such as a text editor, debugger, profiler, and interactive console. You can execute **Spyder** using the **Anaconda Navigator**. You can find Spyder Tutorials [here](https://www.youtube.com/watch?v=E2Dap5SfXkI&list=PLPonohdiDqg9epClEcXoAPUiK0pN5eRoc&ab_channel=SpyderIDE).

### Python packages
A **Python package** is a collection of files containing Python code (i.e., modules). To execute **nOEN**, the following packages must to be installed:
- **Numpy.** NumPy is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more. For more info and tutorials, click [here](https://numpy.org/).
- **Pandas**. Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language. For more info and tutorials, click [here](https://pandas.pydata.org/).
- **Matplotlib**. Matplotlib is a library for creatinc static, animated and interactive visualizations in Python. For more info and tutorials, click [here](https://matplotlib.org/).
- **SciPy**. SciPy is an open-source software for mathematics, science, and engineering. This package provides algorithms for optimization, integration, interpolation, eigenvalue problems, algebraic equations, differential equations, statistics and many other. For more info and tutorials, click [here](https://scipy.org/).
- **Openpyxl**. Openpyxl is a python library to read/write Excel files. For more info and tutorials, click [here](https://openpyxl.readthedocs.io/en/stable/).

### Installation of packages using Anaconda Navigator
You can install any Python package using the **Anaconda Navigator**. For this, execute the navigator and click to **Environments**. In this section you can install new packages and delete the already installed. For more info, click [here](https://docs.anaconda.com/free/navigator/).

### Installation of packages using pip
**pip** is the package installer for Python. In general, pip installs the minimal instalation requirements automatically, but not the optionals requirements. To install the mentioned packages using pip, you have only to write the following command lines in **Anaconda Prompt or Terminal**:

**NumPy**:
```
pip install numpy
```
**Pandas**:
```
pip install pandas
```
**Matplotlib**:
```
pip install matplotlib
```
**SciPy**:
```
pip install scipy
```
**Openpyxl**:
```
pip install openpyxl
```

## :clipboard: Instructions to run nOEN using Command Line Interface (CLI)
1. Download .zip code. Last version: `v0.4`. [Download package](https://github.com/soundslikealloy/nOEN-py/archive/refs/tags/v0.4.zip).
2. Extract files to a destination (:bulb: Recommendation - Desktop).
3. Open **Anaconda Prompt or Terminal**.
4. Go to the **Code folder<sup>2</sup>** using `cd` command (more info about [Using Terminal](https://docs.anaconda.com/ae-notebooks/user-guide/basic-tasks/apps/use-terminal/?highlight=Using%20Terminal)).
    &#09;<br><sup><sup>2</sup>Code folder: folder with `nOENcmd.py` file (Folder: `/src/nOEN`). </sup>
5. Create Excel file with data following the information included in 'Information Sheet' of template file (`/Data/Template/template.xlsx`) or example file (`/Data/example.xlsx`). You can use any of them. Be sure that data files are in `/Data` folder. The name of file (without extension .xlsx) will be used to call the nOEN package (see next point). 
6. Execute **nOEN** with the command line:
   ```
   python nOENcmd.py -filename FILENAME
   ```
   Where `FILENAME` is the name of Excel (from `/Data` folder) you want analyze (without extension '.xlsx'). 
   For example:
   ```
   python nOENcmd.py -filename example
   ```
   Results from **nOEN** are saved in .npy (as `FILENAME.npy`), .xlsx (as `FILENAME_results.xlsx`) format and/or plotted (see [Results Visualization](#results-visualization)). All nOEN outcomes are saved in `/Results` folder.
   
   **Optional arguments:**
   <table border="0">
       <tr><td>-h, --help</b></td><td> Show help message and optional arguments.</b></td></tr>
       <tr><td>-dim</td><td> Dimensions we want to test. Numbers separated by spaces without parenthesis or brakets.</td></tr>
       <tr><td>-infoinocula</td><td> Information of inocula (or time 0) provided.</td></tr>
       <tr><td>-noExcel</td><td> Save nOEN results only in '.npy' format.</td></tr>
       <tr><td>-onlyExcel</td><td> Create Excel file with existing nOEN results (saved in '.npy' format).</td></tr>
       <tr><td>-varSelect</td><td> Variables we want to write and/or plot. Name of variables separated by spaces without parenthesis or brakets.</td></tr>
       <tr><td>-onlysig</td><td> Only significant results (p < 0.05) are written and/or plotted.</td></tr>
       <tr><td>-noFigures</td><td> No plotting. Outcomes from nOEN are only saved in Excel.</td></tr>
       <tr><td>-onlyFigures</td><td> Outcomes from nOEN are only plotted, not saved in Excel.</td></tr>
   </table>

   ```
   python nOENcmd.py -h
   python nOENcmd.py -filename template -onlysig
   python nOENcmd.py -filename template -varSelect S3 S5
   python nOENcmd.py -filename template -dim 2 4 5
   python nOENcmd.py -filename template -infoinocula
   python nOENcmd.py -filename template -infoinocula -dim 2 4 5
   python nOENcmd.py -filename template -dim 2 4 5 -noExcel
   python nOENcmd.py -filename template -noExcel
   python nOENcmd.py -filename template -dim 2 4 5 -onlyExcel
   python nOENcmd.py -filename template -dim 2 4 5 -onlyExcel -varSelect S3 S5
   python nOENcmd.py -filename template -dim 2 4 5 -onlyExcel -varSelect S3 S5 -onlysig
   ```

## Results Visualization
### Ecological Grid
For now, only one type of representation is included in **nOEN platform** - the Ecological Grid. For two joint variables (N=2), all data trends are represented in a 2D grid. For more than two joint variables (N>2), each data trend is represented by a separate plot. All plots are saved in new folder started with the name of Excel file in `\Results\` folder (by default, plots are created and saved). Since there is only one type of results visualization, it is not necessary to specify the type of representation. To disable the creation and saving of plots, add `-noFigures` to the command line. If only plots are desired, add `-onlyFigures` to the command line. As when writting results in Excel, the user can specify the dimensions, variables and only significative trends to be represented.
```
python nOENcmd.py -filename template -noFigures
python nOENcmd.py -filename template -onlyFigures
python nOENcmd.py -filename template -onlyFigures -varSelect S3 S5
python nOENcmd.py -filename template -onlyFigures -varSelect S3 S5 -dim 2 4 5
python nOENcmd.py -filename template -onlyFigures -varSelect S3 S5 -dim 2 4 5 -onlysig
```

## Contact

**Eloi Martinez-Rabert**. :envelope: eloi.mrp@gmail.com

### References
[^1]: Martinez-Rabert, E. (2023). *arXiv (preprint)*. doi: [10.48550/arXiv.2308.01062](https://doi.org/10.48550/arXiv.2308.01062)<br>
[^2]: Kendall, M. G. (1938). *Biometrika*. doi: [10.1093/biomet/30.1-2.81](https://doi.org/10.1093/biomet/30.1-2.81)<br>
