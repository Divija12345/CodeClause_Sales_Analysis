{
  "metadata": {
    "kernelspec": {
      "language": "python",
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "pygments_lexer": "ipython3",
      "nbconvert_exporter": "python",
      "version": "3.6.4",
      "file_extension": ".py",
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "name": "python",
      "mimetype": "text/x-python"
    },
    "colab": {
      "name": "Sales-Analysis",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    }
  },
  "nbformat_minor": 0,
  "nbformat": 4,
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Divija12345/CodeClause_Sales_Analysis/blob/master/Sales_Analysis.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Importing Dependencies**"
      ],
      "metadata": {
        "id": "Cw3uojoq7B1U"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Loading to a pandas dataframe"
      ],
      "metadata": {
        "id": "NuZBZmab9BGx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W9muXl-k7GAM",
        "outputId": "2490bd52-b396-48ad-dad5-3d34d351785c"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n"
      ],
      "metadata": {
        "id": "BDaztn-0sSNK",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:30.071812Z",
          "iopub.execute_input": "2022-06-23T03:42:30.072429Z",
          "iopub.status.idle": "2022-06-23T03:42:31.020834Z",
          "shell.execute_reply.started": "2022-06-23T03:42:30.072381Z",
          "shell.execute_reply": "2022-06-23T03:42:31.01995Z"
        },
        "trusted": true
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sales = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/SalesAnalysis.csv')"
      ],
      "metadata": {
        "id": "87G1rk0bse0U",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.023257Z",
          "iopub.execute_input": "2022-06-23T03:42:31.023648Z",
          "iopub.status.idle": "2022-06-23T03:42:31.04819Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.023606Z",
          "shell.execute_reply": "2022-06-23T03:42:31.04721Z"
        },
        "trusted": true
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sales.head()"
      ],
      "metadata": {
        "id": "tLYA-UFmsqME",
        "outputId": "b893bdb5-f342-485c-da29-36f990348044",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.049675Z",
          "iopub.execute_input": "2022-06-23T03:42:31.050209Z",
          "iopub.status.idle": "2022-06-23T03:42:31.07824Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.050166Z",
          "shell.execute_reply": "2022-06-23T03:42:31.077304Z"
        },
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 354
        }
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "    Invoice ID Branch       City Customer type  Gender  \\\n",
              "0  750-67-8428      A     Yangon        Member  Female   \n",
              "1  226-31-3081      C  Naypyitaw        Normal  Female   \n",
              "2  631-41-3108      A     Yangon        Normal    Male   \n",
              "3  123-19-1176      A     Yangon        Member    Male   \n",
              "4  373-73-7910      A     Yangon        Normal    Male   \n",
              "\n",
              "             Product line  Unit price  Quantity   Tax 5%     Total       Date  \\\n",
              "0       Health and beauty       74.69         7  26.1415  548.9715   1/5/2019   \n",
              "1  Electronic accessories       15.28         5   3.8200   80.2200   3/8/2019   \n",
              "2      Home and lifestyle       46.33         7  16.2155  340.5255   3/3/2019   \n",
              "3       Health and beauty       58.22         8  23.2880  489.0480  1/27/2019   \n",
              "4       Sports and travel       86.31         7  30.2085  634.3785   2/8/2019   \n",
              "\n",
              "    Time      Payment    cogs  gross margin percentage  gross income  Rating  \n",
              "0  13:08      Ewallet  522.83                 4.761905       26.1415     9.1  \n",
              "1  10:29         Cash   76.40                 4.761905        3.8200     9.6  \n",
              "2  13:23  Credit card  324.31                 4.761905       16.2155     7.4  \n",
              "3  20:33      Ewallet  465.76                 4.761905       23.2880     8.4  \n",
              "4  10:37      Ewallet  604.17                 4.761905       30.2085     5.3  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-4f610e37-816a-439f-b526-f4726b549266\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Invoice ID</th>\n",
              "      <th>Branch</th>\n",
              "      <th>City</th>\n",
              "      <th>Customer type</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Product line</th>\n",
              "      <th>Unit price</th>\n",
              "      <th>Quantity</th>\n",
              "      <th>Tax 5%</th>\n",
              "      <th>Total</th>\n",
              "      <th>Date</th>\n",
              "      <th>Time</th>\n",
              "      <th>Payment</th>\n",
              "      <th>cogs</th>\n",
              "      <th>gross margin percentage</th>\n",
              "      <th>gross income</th>\n",
              "      <th>Rating</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>750-67-8428</td>\n",
              "      <td>A</td>\n",
              "      <td>Yangon</td>\n",
              "      <td>Member</td>\n",
              "      <td>Female</td>\n",
              "      <td>Health and beauty</td>\n",
              "      <td>74.69</td>\n",
              "      <td>7</td>\n",
              "      <td>26.1415</td>\n",
              "      <td>548.9715</td>\n",
              "      <td>1/5/2019</td>\n",
              "      <td>13:08</td>\n",
              "      <td>Ewallet</td>\n",
              "      <td>522.83</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>26.1415</td>\n",
              "      <td>9.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>226-31-3081</td>\n",
              "      <td>C</td>\n",
              "      <td>Naypyitaw</td>\n",
              "      <td>Normal</td>\n",
              "      <td>Female</td>\n",
              "      <td>Electronic accessories</td>\n",
              "      <td>15.28</td>\n",
              "      <td>5</td>\n",
              "      <td>3.8200</td>\n",
              "      <td>80.2200</td>\n",
              "      <td>3/8/2019</td>\n",
              "      <td>10:29</td>\n",
              "      <td>Cash</td>\n",
              "      <td>76.40</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>3.8200</td>\n",
              "      <td>9.6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>631-41-3108</td>\n",
              "      <td>A</td>\n",
              "      <td>Yangon</td>\n",
              "      <td>Normal</td>\n",
              "      <td>Male</td>\n",
              "      <td>Home and lifestyle</td>\n",
              "      <td>46.33</td>\n",
              "      <td>7</td>\n",
              "      <td>16.2155</td>\n",
              "      <td>340.5255</td>\n",
              "      <td>3/3/2019</td>\n",
              "      <td>13:23</td>\n",
              "      <td>Credit card</td>\n",
              "      <td>324.31</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>16.2155</td>\n",
              "      <td>7.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>123-19-1176</td>\n",
              "      <td>A</td>\n",
              "      <td>Yangon</td>\n",
              "      <td>Member</td>\n",
              "      <td>Male</td>\n",
              "      <td>Health and beauty</td>\n",
              "      <td>58.22</td>\n",
              "      <td>8</td>\n",
              "      <td>23.2880</td>\n",
              "      <td>489.0480</td>\n",
              "      <td>1/27/2019</td>\n",
              "      <td>20:33</td>\n",
              "      <td>Ewallet</td>\n",
              "      <td>465.76</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>23.2880</td>\n",
              "      <td>8.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>373-73-7910</td>\n",
              "      <td>A</td>\n",
              "      <td>Yangon</td>\n",
              "      <td>Normal</td>\n",
              "      <td>Male</td>\n",
              "      <td>Sports and travel</td>\n",
              "      <td>86.31</td>\n",
              "      <td>7</td>\n",
              "      <td>30.2085</td>\n",
              "      <td>634.3785</td>\n",
              "      <td>2/8/2019</td>\n",
              "      <td>10:37</td>\n",
              "      <td>Ewallet</td>\n",
              "      <td>604.17</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>30.2085</td>\n",
              "      <td>5.3</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-4f610e37-816a-439f-b526-f4726b549266')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-4f610e37-816a-439f-b526-f4726b549266 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-4f610e37-816a-439f-b526-f4726b549266');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sales.shape # To check number of rows and columns"
      ],
      "metadata": {
        "id": "kT6p3iJDs6U5",
        "outputId": "f9ef3931-18bf-4512-8f86-f74f16bf3ab5",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.079451Z",
          "iopub.execute_input": "2022-06-23T03:42:31.079728Z",
          "iopub.status.idle": "2022-06-23T03:42:31.084863Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.079703Z",
          "shell.execute_reply": "2022-06-23T03:42:31.084201Z"
        },
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(1000, 17)"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sales.columns"
      ],
      "metadata": {
        "id": "50xeAXhes7x2",
        "outputId": "3a264bf5-04e9-4d65-f1fb-1d0f128b9606",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.087285Z",
          "iopub.execute_input": "2022-06-23T03:42:31.087765Z",
          "iopub.status.idle": "2022-06-23T03:42:31.097182Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.087736Z",
          "shell.execute_reply": "2022-06-23T03:42:31.096362Z"
        },
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender',\n",
              "       'Product line', 'Unit price', 'Quantity', 'Tax 5%', 'Total', 'Date',\n",
              "       'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income',\n",
              "       'Rating'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Dataset Information"
      ],
      "metadata": {
        "id": "cpnb9y_R9LGM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sales.dtypes"
      ],
      "metadata": {
        "id": "xjdbJRmgs97V",
        "outputId": "2ab187d8-ed68-4cbd-f94d-5c088bf52372",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.09954Z",
          "iopub.execute_input": "2022-06-23T03:42:31.100064Z",
          "iopub.status.idle": "2022-06-23T03:42:31.110937Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.100033Z",
          "shell.execute_reply": "2022-06-23T03:42:31.110212Z"
        },
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Invoice ID                  object\n",
              "Branch                      object\n",
              "City                        object\n",
              "Customer type               object\n",
              "Gender                      object\n",
              "Product line                object\n",
              "Unit price                 float64\n",
              "Quantity                     int64\n",
              "Tax 5%                     float64\n",
              "Total                      float64\n",
              "Date                        object\n",
              "Time                        object\n",
              "Payment                     object\n",
              "cogs                       float64\n",
              "gross margin percentage    float64\n",
              "gross income               float64\n",
              "Rating                     float64\n",
              "dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Well here date is object , let's convert it into Datetime"
      ],
      "metadata": {
        "id": "WtQ7KIbDtBE4"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sales['Date'] = pd.to_datetime(sales['Date'])"
      ],
      "metadata": {
        "id": "x_L3arKAs_mn",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.112384Z",
          "iopub.execute_input": "2022-06-23T03:42:31.112858Z",
          "iopub.status.idle": "2022-06-23T03:42:31.133265Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.112829Z",
          "shell.execute_reply": "2022-06-23T03:42:31.132408Z"
        },
        "trusted": true
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sales['Date']"
      ],
      "metadata": {
        "id": "Ht42r9XXtbaV",
        "outputId": "3486a44c-d35c-4d91-9d92-b6d0a61148e0",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.134359Z",
          "iopub.execute_input": "2022-06-23T03:42:31.134748Z",
          "iopub.status.idle": "2022-06-23T03:42:31.141967Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.134721Z",
          "shell.execute_reply": "2022-06-23T03:42:31.141201Z"
        },
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0     2019-01-05\n",
              "1     2019-03-08\n",
              "2     2019-03-03\n",
              "3     2019-01-27\n",
              "4     2019-02-08\n",
              "         ...    \n",
              "995   2019-01-29\n",
              "996   2019-03-02\n",
              "997   2019-02-09\n",
              "998   2019-02-22\n",
              "999   2019-02-18\n",
              "Name: Date, Length: 1000, dtype: datetime64[ns]"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sales.dtypes"
      ],
      "metadata": {
        "id": "-3aG_hbKtgUd",
        "outputId": "653c31dd-f5a9-4bbc-f4a8-1aeb8db915ad",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.143188Z",
          "iopub.execute_input": "2022-06-23T03:42:31.14359Z",
          "iopub.status.idle": "2022-06-23T03:42:31.153428Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.143554Z",
          "shell.execute_reply": "2022-06-23T03:42:31.152475Z"
        },
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Invoice ID                         object\n",
              "Branch                             object\n",
              "City                               object\n",
              "Customer type                      object\n",
              "Gender                             object\n",
              "Product line                       object\n",
              "Unit price                        float64\n",
              "Quantity                            int64\n",
              "Tax 5%                            float64\n",
              "Total                             float64\n",
              "Date                       datetime64[ns]\n",
              "Time                               object\n",
              "Payment                            object\n",
              "cogs                              float64\n",
              "gross margin percentage           float64\n",
              "gross income                      float64\n",
              "Rating                            float64\n",
              "dtype: object"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Finally , we have changed date to datetime from object"
      ],
      "metadata": {
        "id": "-3hxszAttkGQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sales.set_index('Date',inplace =True)"
      ],
      "metadata": {
        "id": "9sQn0pEith4-",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.155345Z",
          "iopub.execute_input": "2022-06-23T03:42:31.156032Z",
          "iopub.status.idle": "2022-06-23T03:42:31.161885Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.155987Z",
          "shell.execute_reply": "2022-06-23T03:42:31.161178Z"
        },
        "trusted": true
      },
      "execution_count": 11,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sales.head()"
      ],
      "metadata": {
        "id": "W959ox-9wYnk",
        "outputId": "14f601ec-ec59-499b-b7bb-d70796050832",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.163184Z",
          "iopub.execute_input": "2022-06-23T03:42:31.163443Z",
          "iopub.status.idle": "2022-06-23T03:42:31.189423Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.163418Z",
          "shell.execute_reply": "2022-06-23T03:42:31.188384Z"
        },
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 386
        }
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "             Invoice ID Branch       City Customer type  Gender  \\\n",
              "Date                                                              \n",
              "2019-01-05  750-67-8428      A     Yangon        Member  Female   \n",
              "2019-03-08  226-31-3081      C  Naypyitaw        Normal  Female   \n",
              "2019-03-03  631-41-3108      A     Yangon        Normal    Male   \n",
              "2019-01-27  123-19-1176      A     Yangon        Member    Male   \n",
              "2019-02-08  373-73-7910      A     Yangon        Normal    Male   \n",
              "\n",
              "                      Product line  Unit price  Quantity   Tax 5%     Total  \\\n",
              "Date                                                                          \n",
              "2019-01-05       Health and beauty       74.69         7  26.1415  548.9715   \n",
              "2019-03-08  Electronic accessories       15.28         5   3.8200   80.2200   \n",
              "2019-03-03      Home and lifestyle       46.33         7  16.2155  340.5255   \n",
              "2019-01-27       Health and beauty       58.22         8  23.2880  489.0480   \n",
              "2019-02-08       Sports and travel       86.31         7  30.2085  634.3785   \n",
              "\n",
              "             Time      Payment    cogs  gross margin percentage  gross income  \\\n",
              "Date                                                                            \n",
              "2019-01-05  13:08      Ewallet  522.83                 4.761905       26.1415   \n",
              "2019-03-08  10:29         Cash   76.40                 4.761905        3.8200   \n",
              "2019-03-03  13:23  Credit card  324.31                 4.761905       16.2155   \n",
              "2019-01-27  20:33      Ewallet  465.76                 4.761905       23.2880   \n",
              "2019-02-08  10:37      Ewallet  604.17                 4.761905       30.2085   \n",
              "\n",
              "            Rating  \n",
              "Date                \n",
              "2019-01-05     9.1  \n",
              "2019-03-08     9.6  \n",
              "2019-03-03     7.4  \n",
              "2019-01-27     8.4  \n",
              "2019-02-08     5.3  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b1c9ac39-9306-4827-ac2f-b57d3e57f896\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Invoice ID</th>\n",
              "      <th>Branch</th>\n",
              "      <th>City</th>\n",
              "      <th>Customer type</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Product line</th>\n",
              "      <th>Unit price</th>\n",
              "      <th>Quantity</th>\n",
              "      <th>Tax 5%</th>\n",
              "      <th>Total</th>\n",
              "      <th>Time</th>\n",
              "      <th>Payment</th>\n",
              "      <th>cogs</th>\n",
              "      <th>gross margin percentage</th>\n",
              "      <th>gross income</th>\n",
              "      <th>Rating</th>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>Date</th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "      <th></th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>2019-01-05</th>\n",
              "      <td>750-67-8428</td>\n",
              "      <td>A</td>\n",
              "      <td>Yangon</td>\n",
              "      <td>Member</td>\n",
              "      <td>Female</td>\n",
              "      <td>Health and beauty</td>\n",
              "      <td>74.69</td>\n",
              "      <td>7</td>\n",
              "      <td>26.1415</td>\n",
              "      <td>548.9715</td>\n",
              "      <td>13:08</td>\n",
              "      <td>Ewallet</td>\n",
              "      <td>522.83</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>26.1415</td>\n",
              "      <td>9.1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-03-08</th>\n",
              "      <td>226-31-3081</td>\n",
              "      <td>C</td>\n",
              "      <td>Naypyitaw</td>\n",
              "      <td>Normal</td>\n",
              "      <td>Female</td>\n",
              "      <td>Electronic accessories</td>\n",
              "      <td>15.28</td>\n",
              "      <td>5</td>\n",
              "      <td>3.8200</td>\n",
              "      <td>80.2200</td>\n",
              "      <td>10:29</td>\n",
              "      <td>Cash</td>\n",
              "      <td>76.40</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>3.8200</td>\n",
              "      <td>9.6</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-03-03</th>\n",
              "      <td>631-41-3108</td>\n",
              "      <td>A</td>\n",
              "      <td>Yangon</td>\n",
              "      <td>Normal</td>\n",
              "      <td>Male</td>\n",
              "      <td>Home and lifestyle</td>\n",
              "      <td>46.33</td>\n",
              "      <td>7</td>\n",
              "      <td>16.2155</td>\n",
              "      <td>340.5255</td>\n",
              "      <td>13:23</td>\n",
              "      <td>Credit card</td>\n",
              "      <td>324.31</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>16.2155</td>\n",
              "      <td>7.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-01-27</th>\n",
              "      <td>123-19-1176</td>\n",
              "      <td>A</td>\n",
              "      <td>Yangon</td>\n",
              "      <td>Member</td>\n",
              "      <td>Male</td>\n",
              "      <td>Health and beauty</td>\n",
              "      <td>58.22</td>\n",
              "      <td>8</td>\n",
              "      <td>23.2880</td>\n",
              "      <td>489.0480</td>\n",
              "      <td>20:33</td>\n",
              "      <td>Ewallet</td>\n",
              "      <td>465.76</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>23.2880</td>\n",
              "      <td>8.4</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2019-02-08</th>\n",
              "      <td>373-73-7910</td>\n",
              "      <td>A</td>\n",
              "      <td>Yangon</td>\n",
              "      <td>Normal</td>\n",
              "      <td>Male</td>\n",
              "      <td>Sports and travel</td>\n",
              "      <td>86.31</td>\n",
              "      <td>7</td>\n",
              "      <td>30.2085</td>\n",
              "      <td>634.3785</td>\n",
              "      <td>10:37</td>\n",
              "      <td>Ewallet</td>\n",
              "      <td>604.17</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>30.2085</td>\n",
              "      <td>5.3</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b1c9ac39-9306-4827-ac2f-b57d3e57f896')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-b1c9ac39-9306-4827-ac2f-b57d3e57f896 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-b1c9ac39-9306-4827-ac2f-b57d3e57f896');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sales.describe()  # Statistical Summary"
      ],
      "metadata": {
        "id": "atRsSXGkwlp2",
        "outputId": "aae2d0ff-621e-40ee-b421-7fa742ce558c",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.190738Z",
          "iopub.execute_input": "2022-06-23T03:42:31.191322Z",
          "iopub.status.idle": "2022-06-23T03:42:31.228476Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.19128Z",
          "shell.execute_reply": "2022-06-23T03:42:31.227508Z"
        },
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 300
        }
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        Unit price     Quantity       Tax 5%        Total        cogs  \\\n",
              "count  1000.000000  1000.000000  1000.000000  1000.000000  1000.00000   \n",
              "mean     55.672130     5.510000    15.379369   322.966749   307.58738   \n",
              "std      26.494628     2.923431    11.708825   245.885335   234.17651   \n",
              "min      10.080000     1.000000     0.508500    10.678500    10.17000   \n",
              "25%      32.875000     3.000000     5.924875   124.422375   118.49750   \n",
              "50%      55.230000     5.000000    12.088000   253.848000   241.76000   \n",
              "75%      77.935000     8.000000    22.445250   471.350250   448.90500   \n",
              "max      99.960000    10.000000    49.650000  1042.650000   993.00000   \n",
              "\n",
              "       gross margin percentage  gross income      Rating  \n",
              "count              1000.000000   1000.000000  1000.00000  \n",
              "mean                  4.761905     15.379369     6.97270  \n",
              "std                   0.000000     11.708825     1.71858  \n",
              "min                   4.761905      0.508500     4.00000  \n",
              "25%                   4.761905      5.924875     5.50000  \n",
              "50%                   4.761905     12.088000     7.00000  \n",
              "75%                   4.761905     22.445250     8.50000  \n",
              "max                   4.761905     49.650000    10.00000  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-23259ea9-ff04-4458-b5d2-3b0cea47c56e\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Unit price</th>\n",
              "      <th>Quantity</th>\n",
              "      <th>Tax 5%</th>\n",
              "      <th>Total</th>\n",
              "      <th>cogs</th>\n",
              "      <th>gross margin percentage</th>\n",
              "      <th>gross income</th>\n",
              "      <th>Rating</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>1000.000000</td>\n",
              "      <td>1000.000000</td>\n",
              "      <td>1000.000000</td>\n",
              "      <td>1000.000000</td>\n",
              "      <td>1000.00000</td>\n",
              "      <td>1000.000000</td>\n",
              "      <td>1000.000000</td>\n",
              "      <td>1000.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>55.672130</td>\n",
              "      <td>5.510000</td>\n",
              "      <td>15.379369</td>\n",
              "      <td>322.966749</td>\n",
              "      <td>307.58738</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>15.379369</td>\n",
              "      <td>6.97270</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>26.494628</td>\n",
              "      <td>2.923431</td>\n",
              "      <td>11.708825</td>\n",
              "      <td>245.885335</td>\n",
              "      <td>234.17651</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>11.708825</td>\n",
              "      <td>1.71858</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>10.080000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>0.508500</td>\n",
              "      <td>10.678500</td>\n",
              "      <td>10.17000</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>0.508500</td>\n",
              "      <td>4.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>32.875000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>5.924875</td>\n",
              "      <td>124.422375</td>\n",
              "      <td>118.49750</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>5.924875</td>\n",
              "      <td>5.50000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>55.230000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>12.088000</td>\n",
              "      <td>253.848000</td>\n",
              "      <td>241.76000</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>12.088000</td>\n",
              "      <td>7.00000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>77.935000</td>\n",
              "      <td>8.000000</td>\n",
              "      <td>22.445250</td>\n",
              "      <td>471.350250</td>\n",
              "      <td>448.90500</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>22.445250</td>\n",
              "      <td>8.50000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>99.960000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>49.650000</td>\n",
              "      <td>1042.650000</td>\n",
              "      <td>993.00000</td>\n",
              "      <td>4.761905</td>\n",
              "      <td>49.650000</td>\n",
              "      <td>10.00000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-23259ea9-ff04-4458-b5d2-3b0cea47c56e')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "        \n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "      \n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-23259ea9-ff04-4458-b5d2-3b0cea47c56e button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-23259ea9-ff04-4458-b5d2-3b0cea47c56e');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n",
              "  "
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sales.isnull().sum() # To check null values"
      ],
      "metadata": {
        "id": "TIeDaeDS1kzk",
        "outputId": "6b66d82e-43bb-45df-aa9e-608d401ce004",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.229659Z",
          "iopub.execute_input": "2022-06-23T03:42:31.230207Z",
          "iopub.status.idle": "2022-06-23T03:42:31.23919Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.230167Z",
          "shell.execute_reply": "2022-06-23T03:42:31.238061Z"
        },
        "trusted": true,
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Invoice ID                 0\n",
              "Branch                     0\n",
              "City                       0\n",
              "Customer type              0\n",
              "Gender                     0\n",
              "Product line               0\n",
              "Unit price                 0\n",
              "Quantity                   0\n",
              "Tax 5%                     0\n",
              "Total                      0\n",
              "Time                       0\n",
              "Payment                    0\n",
              "cogs                       0\n",
              "gross margin percentage    0\n",
              "gross income               0\n",
              "Rating                     0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 14
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "corrmat=sales.corr()\n",
        "plt.figure(figsize=(7,7))\n",
        "sns.heatmap(corrmat,vmax=0.9, square=True )\n",
        "plt.show"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 527
        },
        "id": "Ei_rZD_JXDss",
        "outputId": "20904b00-6730-48d1-b024-e2df3c0652f3"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<function matplotlib.pyplot.show>"
            ]
          },
          "metadata": {},
          "execution_count": 22
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 504x504 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Lets's first handle Unit Price column by using mean value"
      ],
      "metadata": {
        "id": "jIBH2qIDS8ga"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "avg_unit_price = sales[\"Unit price\"].astype(\"float\").mean(axis=0)\n",
        "sales[\"Unit price\"].replace(np.nan, avg_unit_price, inplace=True)"
      ],
      "metadata": {
        "id": "OW3tvfhvM6Tf",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.240729Z",
          "iopub.execute_input": "2022-06-23T03:42:31.241086Z",
          "iopub.status.idle": "2022-06-23T03:42:31.251959Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.240958Z",
          "shell.execute_reply": "2022-06-23T03:42:31.251236Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "For Quantity we will use Mode value"
      ],
      "metadata": {
        "id": "tb7ZgEc2TObJ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from scipy import stats\n",
        "mode=stats.mode(sales['Quantity'])\n",
        "\n",
        "print(mode)"
      ],
      "metadata": {
        "id": "_N2TR-k8OCdK",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.253198Z",
          "iopub.execute_input": "2022-06-23T03:42:31.253753Z",
          "iopub.status.idle": "2022-06-23T03:42:31.264237Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.253712Z",
          "shell.execute_reply": "2022-06-23T03:42:31.263017Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sales['Quantity'].replace(np.nan, \"mode\", inplace=True)"
      ],
      "metadata": {
        "id": "yeA-G_oFOE5h",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.265794Z",
          "iopub.execute_input": "2022-06-23T03:42:31.26622Z",
          "iopub.status.idle": "2022-06-23T03:42:31.273722Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.266178Z",
          "shell.execute_reply": "2022-06-23T03:42:31.272742Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "For rest remaining values we will simply drop them"
      ],
      "metadata": {
        "id": "YPRTb3WQTXpf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sales.dropna(inplace=True)"
      ],
      "metadata": {
        "id": "-ytZqC8wOVHT",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.27522Z",
          "iopub.execute_input": "2022-06-23T03:42:31.275805Z",
          "iopub.status.idle": "2022-06-23T03:42:31.304065Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.275754Z",
          "shell.execute_reply": "2022-06-23T03:42:31.303224Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sales.isnull().sum() # Finally we can see No null values"
      ],
      "metadata": {
        "id": "fomjUOq8POAI",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.305335Z",
          "iopub.execute_input": "2022-06-23T03:42:31.305913Z",
          "iopub.status.idle": "2022-06-23T03:42:31.315774Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.305869Z",
          "shell.execute_reply": "2022-06-23T03:42:31.31498Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sales.corr()"
      ],
      "metadata": {
        "id": "0DD1bkGEUl8s",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.317145Z",
          "iopub.execute_input": "2022-06-23T03:42:31.317772Z",
          "iopub.status.idle": "2022-06-23T03:42:31.34136Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.317731Z",
          "shell.execute_reply": "2022-06-23T03:42:31.340221Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "np.round(sales.corr(),2)"
      ],
      "metadata": {
        "id": "mMVIqdJLUk_K",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.342633Z",
          "iopub.execute_input": "2022-06-23T03:42:31.342911Z",
          "iopub.status.idle": "2022-06-23T03:42:31.362102Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.342886Z",
          "shell.execute_reply": "2022-06-23T03:42:31.361392Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **EXPLORATORY DATA ANALYSIS**"
      ],
      "metadata": {
        "id": "dgHJp69bTj6p"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(dpi=125)\n",
        "sns.heatmap(np.round(sales.corr(),2),annot=True)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "GqaxUnndUFvh",
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.363181Z",
          "iopub.execute_input": "2022-06-23T03:42:31.363603Z",
          "iopub.status.idle": "2022-06-23T03:42:31.837575Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.363575Z",
          "shell.execute_reply": "2022-06-23T03:42:31.836869Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**The best correlated are Tax 5%, Total, Gross Income and cogs i.e Cost of Goods sold with a correlation of 1.**\n",
        "\n",
        "**Also, the above mentioned all has a good correlation of 0.71 with Quantity**\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "EgQy8Pbx7B1c"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(12,6),dpi=100)\n",
        "sns.regplot(x='Quantity',y='cogs',data=sales,color='green')\n",
        "plt.xlabel('Quantity')\n",
        "plt.ylabel('Cost of Goods Sale')\n",
        "plt.title('Quantity v Cost of Goods Sale',fontsize=15)\n",
        "plt.show()"
      ],
      "metadata": {
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:32.166638Z",
          "iopub.execute_input": "2022-06-23T03:42:32.167321Z",
          "iopub.status.idle": "2022-06-23T03:42:32.498573Z",
          "shell.execute_reply.started": "2022-06-23T03:42:32.167279Z",
          "shell.execute_reply": "2022-06-23T03:42:32.497765Z"
        },
        "trusted": true,
        "id": "cQu7jXPl7B1c"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(dpi=125)\n",
        "sns.countplot(sales['City'])\n",
        "plt.xlabel('City')\n",
        "plt.ylabel('Count')\n",
        "plt.title('Which City is most busy?')\n",
        "A,B,C =sales.City.value_counts()\n",
        "\n",
        "print('Yangon -',A)\n",
        "print('Naypyitow -',C)\n",
        "print('Mandalay -',B)\n",
        "plt.show()"
      ],
      "metadata": {
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:34.616362Z",
          "iopub.execute_input": "2022-06-23T03:42:34.616616Z",
          "iopub.status.idle": "2022-06-23T03:42:34.758791Z",
          "shell.execute_reply.started": "2022-06-23T03:42:34.616593Z",
          "shell.execute_reply": "2022-06-23T03:42:34.757774Z"
        },
        "trusted": true,
        "id": "n7tgDbkA7B1f"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(12,6),dpi=100)\n",
        "sns.regplot(x='Unit price',y='gross income',data=sales,color='blue')\n",
        "plt.xlabel('Unit Price')\n",
        "plt.ylabel('Gross Income')\n",
        "plt.title('Unit Price v Gross Income',fontsize=15)\n",
        "plt.show()"
      ],
      "metadata": {
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:32.499764Z",
          "iopub.execute_input": "2022-06-23T03:42:32.500277Z",
          "iopub.status.idle": "2022-06-23T03:42:32.899218Z",
          "shell.execute_reply.started": "2022-06-23T03:42:32.500246Z",
          "shell.execute_reply": "2022-06-23T03:42:32.89851Z"
        },
        "trusted": true,
        "id": "bs9K4SZZ7B1d"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# To see the distribution of different ratings\n",
        "plt.figure(dpi=125) \n",
        "sns.distplot(sales['Rating'],kde=False)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "o-imBfJWxKjS",
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:32.900388Z",
          "iopub.execute_input": "2022-06-23T03:42:32.90087Z",
          "iopub.status.idle": "2022-06-23T03:42:33.062335Z",
          "shell.execute_reply.started": "2022-06-23T03:42:32.900837Z",
          "shell.execute_reply": "2022-06-23T03:42:33.061486Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Let's find the mean rating now"
      ],
      "metadata": {
        "id": "pQ3xN7FoT5kD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# To find Mean Rating\n",
        "plt.figure(dpi=125)\n",
        "sns.distplot(sales['Rating'],kde=False)\n",
        "plt.axvline(x=np.mean(sales['Rating']),c='green',label='Mean Rating')\n",
        "plt.legend()\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "BUEXIr93xlJH",
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:33.06366Z",
          "iopub.execute_input": "2022-06-23T03:42:33.064048Z",
          "iopub.status.idle": "2022-06-23T03:42:33.251017Z",
          "shell.execute_reply.started": "2022-06-23T03:42:33.064008Z",
          "shell.execute_reply": "2022-06-23T03:42:33.250094Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Plotting Histogram for all\n",
        "sales.hist(figsize=(12,12))\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "Hal1dPnqylo1",
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:33.252419Z",
          "iopub.execute_input": "2022-06-23T03:42:33.25269Z",
          "iopub.status.idle": "2022-06-23T03:42:34.325391Z",
          "shell.execute_reply.started": "2022-06-23T03:42:33.252665Z",
          "shell.execute_reply": "2022-06-23T03:42:34.324255Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(figsize=(12,6),dpi=100)\n",
        "sns.regplot(x='Tax 5%',y='gross income',data=sales,color='Red')\n",
        "plt.xlabel('Tax 5%')\n",
        "plt.ylabel('Gross Income')\n",
        "plt.show()"
      ],
      "metadata": {
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:31.83864Z",
          "iopub.execute_input": "2022-06-23T03:42:31.839053Z",
          "iopub.status.idle": "2022-06-23T03:42:32.165152Z",
          "shell.execute_reply.started": "2022-06-23T03:42:31.839011Z",
          "shell.execute_reply": "2022-06-23T03:42:32.164308Z"
        },
        "trusted": true,
        "id": "vyYtXOH17B1c"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "<h2 style='background:brown; border:0; color:white'><center>Analysis of Branch, City and Product Type</center><h2>"
      ],
      "metadata": {
        "id": "HLf4EodRUOPd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Branch Count\n",
        "plt.figure(dpi=125)\n",
        "sns.countplot(sales['Branch'])\n",
        "plt.xlabel('Branch Name')\n",
        "plt.ylabel('Count')\n",
        "plt.title('Which Branch is the most busy?')\n",
        "A,B,C =sales.Branch.value_counts()\n",
        "print('Branch A -',A)\n",
        "print('Branch B -',C)\n",
        "print('Branch C -',B)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "R2jgRqvq0AG-",
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:34.326692Z",
          "iopub.execute_input": "2022-06-23T03:42:34.327039Z",
          "iopub.status.idle": "2022-06-23T03:42:34.467205Z",
          "shell.execute_reply.started": "2022-06-23T03:42:34.327011Z",
          "shell.execute_reply": "2022-06-23T03:42:34.466392Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(dpi=125)\n",
        "sns.countplot(sales['Payment'])\n",
        "plt.xlabel('Payment Method')\n",
        "plt.ylabel('Count')\n",
        "plt.title('Which Payment Method is most used?')\n",
        "A,B,C =sales.Payment.value_counts()\n",
        "\n",
        "print('E-wallet -',A)\n",
        "print('Cash -',B)\n",
        "print('Credit Card -',C)\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "LWYiHT3q1Gp0",
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:34.468529Z",
          "iopub.execute_input": "2022-06-23T03:42:34.468807Z",
          "iopub.status.idle": "2022-06-23T03:42:34.615305Z",
          "shell.execute_reply.started": "2022-06-23T03:42:34.468779Z",
          "shell.execute_reply": "2022-06-23T03:42:34.614468Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(dpi=125)\n",
        "sns.countplot(sales['Gender'])\n",
        "plt.xlabel('Gender')\n",
        "plt.ylabel('Count')\n",
        "plt.title('Count of Gender')\n",
        "A,B =sales.Gender.value_counts()\n",
        "\n",
        "print('Male-',B)\n",
        "print('Female -',A)\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:34.760211Z",
          "iopub.execute_input": "2022-06-23T03:42:34.760516Z",
          "iopub.status.idle": "2022-06-23T03:42:34.987742Z",
          "shell.execute_reply.started": "2022-06-23T03:42:34.76048Z",
          "shell.execute_reply": "2022-06-23T03:42:34.986841Z"
        },
        "trusted": true,
        "id": "TI0pP5_07B1f"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Visualizing a Gender based comparison related to Product Type**"
      ],
      "metadata": {
        "id": "qsUiBPzsjmmY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sns.catplot(x='Product line',y='Unit price',hue='Gender',data=sales,aspect=2)\n",
        "plt.xlabel('Product Type')\n",
        "plt.ylabel('Unit Price')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "-jUshdvkVh-0",
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:34.991446Z",
          "iopub.execute_input": "2022-06-23T03:42:34.991758Z",
          "iopub.status.idle": "2022-06-23T03:42:35.495554Z",
          "shell.execute_reply.started": "2022-06-23T03:42:34.991729Z",
          "shell.execute_reply": "2022-06-23T03:42:35.494452Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sns.catplot(x='Product line',y='Unit price',hue='Gender',data=sales,aspect=2,jitter=False)\n",
        "plt.xlabel('Product Type')\n",
        "plt.ylabel('Unit Price')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "joEH3R_DV3BV",
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:35.497459Z",
          "iopub.execute_input": "2022-06-23T03:42:35.497857Z",
          "iopub.status.idle": "2022-06-23T03:42:35.931247Z",
          "shell.execute_reply.started": "2022-06-23T03:42:35.497815Z",
          "shell.execute_reply": "2022-06-23T03:42:35.930216Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(dpi=125)\n",
        "sns.countplot(y ='Product line', hue = \"Gender\", data = sales) \n",
        "plt.xlabel('Count')\n",
        "plt.ylabel('Product Type')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "XIkyl57aZeaa",
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:35.932621Z",
          "iopub.execute_input": "2022-06-23T03:42:35.93322Z",
          "iopub.status.idle": "2022-06-23T03:42:36.131323Z",
          "shell.execute_reply.started": "2022-06-23T03:42:35.933175Z",
          "shell.execute_reply": "2022-06-23T03:42:36.130307Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Well, In Health & Beauty, Males are much more than Females whereas in Fashion accessories , Food & beverages and Sports & Travel Females are more and in the rest there is not much significant difference.**"
      ],
      "metadata": {
        "id": "CUDiXcud7B1g"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Visualizing a City based comparison related to Product Type**"
      ],
      "metadata": {
        "id": "ZcadlZ4Qj5Pt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sns.catplot(x='Product line',y='Unit price',hue='City',kind='swarm',data=sales,aspect=2)\n",
        "plt.xlabel('Product Type')\n",
        "plt.ylabel('Unit Price')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "koB2-KS8XM2e",
        "_kg_hide-input": false,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:36.13261Z",
          "iopub.execute_input": "2022-06-23T03:42:36.132896Z",
          "iopub.status.idle": "2022-06-23T03:42:36.791066Z",
          "shell.execute_reply.started": "2022-06-23T03:42:36.132868Z",
          "shell.execute_reply": "2022-06-23T03:42:36.790084Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sns.catplot(x='Product line',y='Unit price',hue='City',data=sales,aspect=2,jitter=False)\n",
        "plt.xlabel('Product Type')\n",
        "plt.ylabel('Unit Price')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "oDtkA2JbXvU-",
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:36.792652Z",
          "iopub.execute_input": "2022-06-23T03:42:36.793079Z",
          "iopub.status.idle": "2022-06-23T03:42:37.325773Z",
          "shell.execute_reply.started": "2022-06-23T03:42:36.793037Z",
          "shell.execute_reply": "2022-06-23T03:42:37.324868Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(dpi=125)\n",
        "sns.countplot(y ='Product line', hue = \"City\", data = sales) \n",
        "plt.xlabel('Count')\n",
        "plt.ylabel('Product Type')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "7Lztd3QlY8_Y",
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:37.327511Z",
          "iopub.execute_input": "2022-06-23T03:42:37.327982Z",
          "iopub.status.idle": "2022-06-23T03:42:37.545218Z",
          "shell.execute_reply.started": "2022-06-23T03:42:37.327926Z",
          "shell.execute_reply": "2022-06-23T03:42:37.544236Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Well, Yangon leads at Home & Lifestyle and Electronic accessories.**\n",
        "\n",
        "**Naypyitaw leads at Food & Bevaerages and Fashion accessories.**\n",
        "\n",
        "**Mandalay leads at Sports & Travel and Health & Beauty.**\n"
      ],
      "metadata": {
        "id": "DkdEJTm57B1g"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Finding the most used payment method for Product Type, Branch and City**"
      ],
      "metadata": {
        "id": "U_ODRJH67B1g"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(dpi=125)\n",
        "sns.countplot(y ='Product line', hue = \"Payment\", data = sales) \n",
        "plt.xlabel('Count')\n",
        "plt.ylabel('Product Type')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "6D6Hjo9Ua_Ub",
        "_kg_hide-input": false,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:37.546809Z",
          "iopub.execute_input": "2022-06-23T03:42:37.547095Z",
          "iopub.status.idle": "2022-06-23T03:42:37.764146Z",
          "shell.execute_reply.started": "2022-06-23T03:42:37.547069Z",
          "shell.execute_reply": "2022-06-23T03:42:37.763312Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(dpi=125)\n",
        "sns.countplot(y ='Branch', hue = \"Payment\", data = sales) \n",
        "plt.xlabel('Count')\n",
        "plt.ylabel('Branch')\n",
        "plt.show()"
      ],
      "metadata": {
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:37.765576Z",
          "iopub.execute_input": "2022-06-23T03:42:37.765869Z",
          "iopub.status.idle": "2022-06-23T03:42:37.932451Z",
          "shell.execute_reply.started": "2022-06-23T03:42:37.76584Z",
          "shell.execute_reply": "2022-06-23T03:42:37.931555Z"
        },
        "trusted": true,
        "id": "JDgZonm07B1h"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(dpi=125)\n",
        "sns.countplot(y ='City', hue = \"Payment\", data = sales) \n",
        "plt.xlabel('Count')\n",
        "plt.ylabel('Product Type')\n",
        "plt.show()"
      ],
      "metadata": {
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:37.933823Z",
          "iopub.execute_input": "2022-06-23T03:42:37.934149Z",
          "iopub.status.idle": "2022-06-23T03:42:38.109014Z",
          "shell.execute_reply.started": "2022-06-23T03:42:37.93409Z",
          "shell.execute_reply": "2022-06-23T03:42:38.108048Z"
        },
        "trusted": true,
        "id": "jFVQPmIe7B1h"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Finding Which Branch has better sale for a particular product type**"
      ],
      "metadata": {
        "id": "E2TL-B7X7B1h"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "plt.figure(dpi=125)\n",
        "sns.countplot(y ='Product line', hue = \"Branch\", data = sales) \n",
        "plt.xlabel('Count')\n",
        "plt.ylabel('Product Type')\n",
        "plt.show()"
      ],
      "metadata": {
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:38.110068Z",
          "iopub.execute_input": "2022-06-23T03:42:38.110368Z",
          "iopub.status.idle": "2022-06-23T03:42:38.326057Z",
          "shell.execute_reply.started": "2022-06-23T03:42:38.110341Z",
          "shell.execute_reply": "2022-06-23T03:42:38.32521Z"
        },
        "trusted": true,
        "id": "zCxrcWhT7B1h"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Boxen Plot for Rating and Quantity**\n",
        "\n",
        "**What is Boxen Plot?**\n",
        "\n",
        "**The Boxen plot is very similar to box plot, except for the fact that it plots different quartile values. By plotting different quartile values, we are able to understand the shape of the distribution particularly in the head end and tail end.**"
      ],
      "metadata": {
        "id": "hCWimqDD7B1h"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "sns.catplot(y ='Rating',x='Quantity', data = sales,kind='boxen',aspect=3) \n",
        "plt.xlabel('Quantity')\n",
        "plt.ylabel('Rating')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "FBsfVofFbW2b",
        "_kg_hide-input": true,
        "execution": {
          "iopub.status.busy": "2022-06-23T03:42:38.327425Z",
          "iopub.execute_input": "2022-06-23T03:42:38.327706Z",
          "iopub.status.idle": "2022-06-23T03:42:38.640925Z",
          "shell.execute_reply.started": "2022-06-23T03:42:38.327679Z",
          "shell.execute_reply": "2022-06-23T03:42:38.640207Z"
        },
        "trusted": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        ""
      ],
      "metadata": {
        "id": "JhVkIZ9A9jRe"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}