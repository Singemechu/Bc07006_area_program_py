{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "08b3c637-c3d0-44ef-a8b8-a5acda74e180",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter list of group1 separated by space:  23 45 67 89 21 43 \n",
      "Enter list of group2 separated by space:  45 89 21 40 98 76\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The intersection of group1 & 2 is:  {89, 21, 45}\n"
     ]
    }
   ],
   "source": [
    "# Sinidu Gemechu\n",
    "\n",
    "\n",
    "#Assesment 1B\n",
    "#Write a Python program called intersect.py. This program will accept the input of \n",
    "#two groups of integers. Each group of integers should be entered as a string in\n",
    "#which integers are separated by spaces. You need to find the integers that exist \n",
    "#in both groups and display them on the screen.\n",
    "\n",
    "Soln;\n",
    "#Enter users number using input ()\n",
    "#strip() removes space between numbers in string\n",
    "#split() separates numbers one from the other\n",
    "#int changes the number to integers by map() then form set (), makes easy to use intersection\n",
    "#operation to find numbers in both groups\n",
    "#Using if else statemnet- if the condition fullfilled,two groups has numbers in common\n",
    "#will show on the screen\n",
    "#len()-to find length of numbers in the intersection set\n",
    "\n",
    "\n",
    "group1= set(map(int, (input(\"Enter list of group1 separated by space: \").strip().split())))\n",
    "group2= set(map(int, (input(\"Enter list of group2 separated by space: \" ).strip().split())))\n",
    "\n",
    "Result= group1.intersection(group2)\n",
    "if  len(group1.intersection(group2))>0:\n",
    "    print(\"The intersection of group1 & 2 is: \" ,Result)\n",
    "else:\n",
    "    print(\"group 1 & 2 has no intersection\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b31696f-22bd-4ee9-abca-0a150f15a97a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
