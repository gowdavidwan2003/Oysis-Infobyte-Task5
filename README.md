## Oysis-Infobyte-Task5
#SALES PREDICTION USING PYTHON


Sales prediction means predicting how much of a product people will buy based on factors
such as the amount you spend to advertise your product, the segment of people you
advertise for, or the platform you are advertising on about your product.

Typically, a product and service-based business always need their Data Scientist to predict
their future sales with every step they take to manipulate the cost of advertising their
product. So let’s start the task of sales prediction with machine learning using Python.

# Sales Prediction Model

This project uses a linear regression model to predict sales based on advertising spend across multiple channels: TV, Radio, and Newspaper.

## Dependencies

The project requires the following Python libraries:
- numpy
- pandas
- seaborn
- matplotlib
- sklearn
- statsmodels

## Dataset

The dataset used in this project is 'Advertising.csv'. It contains the following columns:
- TV: advertising dollars spent on TV for a single product (in thousands of dollars)
- Radio: advertising dollars spent on Radio
- Newspaper: advertising dollars spent on Newspaper
- Sales: sales of a single product in a given market (in thousands of widgets)

## Usage

1. Import the necessary libraries.
2. Load the dataset using pandas.
3. Perform exploratory data analysis (EDA) to understand the data.
4. Split the data into training and testing sets.
5. Fit a linear regression model using statsmodels.
6. Predict sales for new data.

## Results

The linear regression model provides the relationship between 'Sales' and advertising spends on 'TV', 'Radio', and 'Newspaper'. The coefficients of these variables can be interpreted as the change in sales for each additional thousand dollars spent on that advertising medium.

For example, if the coefficient of 'TV' is 0.04, this means that an additional $1,000 spent on TV advertising is associated with an increase in sales of 40 widgets.

## Future Work

This is a simple linear regression model which assumes a linear relationship between the dependent and independent variables. For future work, more complex models could be explored to capture any non-linear relationships in the data.
