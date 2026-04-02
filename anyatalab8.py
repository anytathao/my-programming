# Student Id: 2540830
# Personalized values
d1 = 0
d2 = 3
k = 5
shift = -3
rows_keep = 2

import csv
import math


# Component A
def read_oscillatory_wave_data(filename):
    amplitudes = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            amplitudes.append(float(row[1]))

    mean_amp = sum(amplitudes) / len(amplitudes)
    max_amp = max(amplitudes)

    print(f"Mean Amplitude: {mean_amp}")
    print(f"Max Amplitude: {max_amp}")

    return mean_amp, max_amp

def read_standing_wave_data(filename):
    speeds = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            tension = float(row[1])
            v = math.sqrt(tension / 1)
            speeds.append(v)

    print("Wave Speeds: ", speeds)


# Component B
def create_personalized_oscillatory_file(original, newfile):
    rows = []

    with open(original, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for i, row in enumerate(reader):
            if i >= 5 + d2:
                break
            length = float(row[0])
            amplitude = float(row[1]) + shift
            rows.append([length, amplitude])

    with open(newfile, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)

    return read_oscillatory_wave_data(newfile)

def create_personalized_standing_file(original, newfile):
    rows = []

    with open(original, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        for i, row in enumerate(reader):
            if i >= 4 + rows_keep:
                break
            length = float(row[0])
            tension = float(row[1]) * k
            rows.append([length, tension])

    with open(newfile, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(rows)

    return read_standing_wave_data(newfile)


# Main execution
def main():
    read_oscillatory_wave_data("./lab3/oscillatory_2540830.csv")
    read_standing_wave_data("./lab3/standing_2540830.csv")

    create_personalized_oscillatory_file(
        "./lab3/oscillatory_2540830.csv",
        "./lab3/oscillatory_personalized_2540830.csv"
    )

    create_personalized_standing_file(
        "./lab3/standing_2540830.csv",
        "./lab3/standing_personalized_2540830.csv"
    )

if __name__=="__main__":
    main()