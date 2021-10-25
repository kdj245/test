{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOT3P6/ZesSwsm3jzVguXV+",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/kdj245/test/blob/main/colab.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 430
        },
        "id": "wpCqoOo0NpiG",
        "outputId": "01ede774-33bc-4f92-d89d-6f94c40a6aa4"
      },
      "source": [
        "# 시험용 노트입니다.\n",
        "\n",
        "print(3.141592*10.0*10.0)\n",
        "print((1/100)*1234)\n",
        "\n",
        "\n",
        "\n",
        "import turtle \n",
        "t = turtle.Turtle() \n",
        "t.shape(\"turtle\");  \n",
        "\n",
        "t.forward(100); \n",
        "t.left(60);    \n",
        "t.forward(100);\n",
        "t.left(60);\n",
        "t.forward(100);\n",
        "t.left(60);\n",
        "t.forward(100);\n",
        "t.left(60);\n",
        "t.forward(100);\n",
        "t.left(60);\n",
        "t.forward(100);\n",
        "t.left(60); "
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "314.1592\n",
            "12.34\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "TclError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTclError\u001b[0m                                  Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-4-72c7e4de1bf8>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mturtle\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m \u001b[0mt\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mturtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTurtle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     10\u001b[0m \u001b[0mt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"turtle\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m;\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, shape, undobuffersize, visible)\u001b[0m\n\u001b[1;32m   3810\u001b[0m                  visible=_CFG[\"visible\"]):\n\u001b[1;32m   3811\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mTurtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_screen\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3812\u001b[0;31m             \u001b[0mTurtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_screen\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mScreen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3813\u001b[0m         RawTurtle.__init__(self, Turtle._screen,\n\u001b[1;32m   3814\u001b[0m                            \u001b[0mshape\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mshape\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36mScreen\u001b[0;34m()\u001b[0m\n\u001b[1;32m   3660\u001b[0m     else return the existing one.\"\"\"\n\u001b[1;32m   3661\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mTurtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_screen\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3662\u001b[0;31m         \u001b[0mTurtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_screen\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_Screen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3663\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mTurtle\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_screen\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3664\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m   3676\u001b[0m         \u001b[0;31m# preserved (perhaps by passing it as an optional parameter)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3677\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0m_Screen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_root\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 3678\u001b[0;31m             \u001b[0m_Screen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_root\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_root\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_Root\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   3679\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_root\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtitle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0m_Screen\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_title\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   3680\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_root\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mondestroy\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_destroy\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.7/turtle.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    432\u001b[0m     \u001b[0;34m\"\"\"Root class for Screen based on Tkinter.\"\"\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    433\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 434\u001b[0;31m         \u001b[0mTK\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mTk\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__init__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    435\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    436\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0msetupcanvas\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mwidth\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mheight\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcwidth\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcheight\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/lib/python3.7/tkinter/__init__.py\u001b[0m in \u001b[0;36m__init__\u001b[0;34m(self, screenName, baseName, className, useTk, sync, use)\u001b[0m\n\u001b[1;32m   2021\u001b[0m                 \u001b[0mbaseName\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mbaseName\u001b[0m \u001b[0;34m+\u001b[0m \u001b[0mext\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2022\u001b[0m         \u001b[0minteractive\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2023\u001b[0;31m         \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtk\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_tkinter\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcreate\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mscreenName\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbaseName\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mclassName\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0minteractive\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mwantobjects\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0museTk\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0msync\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0muse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2024\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0museTk\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2025\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_loadtk\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTclError\u001b[0m: no display name and no $DISPLAY environment variable"
          ]
        }
      ]
    }
  ]
}