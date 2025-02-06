import statistics
import matplotlib.pyplot as plt


def veri_analizi(veriler):
    # Aritmetik Ortalama
    ortalama = statistics.mean(veriler)

    # Medyan
    medyan = statistics.median(veriler)

    # Mod (Eğer birden fazla mod varsa, hepsini döndürür)
    try:
        mod = statistics.mode(veriler)
    except statistics.StatisticsError:
        mod = "Veri setinde mod bulunamadı (benzersiz bir mod yok)."

    # Ranj (Aralık)
    ranj = max(veriler) - min(veriler)

    # Standart Sapma
    standart_sapma = statistics.stdev(veriler)

    return ortalama, medyan, mod, ranj, standart_sapma


# Kullanıcıdan veri girişi alalım
veriler = input("Lütfen verileri boşlukla ayırarak girin (örneğin: 1 2 3 4 5): ")
veriler = list(map(float, veriler.split()))  # Girdiyi float listesine dönüştür

# Veri analizini yapalım
ortalama, medyan, mod, ranj, standart_sapma = veri_analizi(veriler)

# Sonuçları ekrana yazdıralım
print(f"Aritmetik Ortalama: {ortalama}")
print(f"Medyan: {medyan}")
print(f"Mod: {mod}")
print(f"Ranj (Aralık): {ranj}")
print(f"Standart Sapma: {standart_sapma}")

# Histogram grafiği oluşturalım
plt.hist(veriler, bins='auto', color='blue', alpha=0.7, rwidth=0.85)
plt.title('Verilerin Histogram Grafiği')
plt.xlabel('Değerler')
plt.ylabel('Frekans')
plt.grid(axis='y', alpha=0.75)
plt.show()
