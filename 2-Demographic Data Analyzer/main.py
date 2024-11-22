from demographic_data_analyzer import demographic_data_analyzer

if __name__ == "__main__":
    results = demographic_data_analyzer()
    for key, value in results.items():
        print(f"{key}: {value}")