# universe_engine.py
from constants import Constants
import time

CONST = Constants()

c = CONST["fundamental_constants.speed_of_light_c"]        # m/s
planck_time = CONST["planck_units.planck_time"]            # s

# Simülasyon parametreleri
distance = 1.0  # metre cinsinden (örnek)
elapsed = 0.0

print("🔭 Foton simülasyonu başlatılıyor...")
print(f"Işık {distance} metreyi kaç Planck zamanında kat eder?")

# Basit zaman döngüsü (gerçek simülasyonlarda bu diferansiyel denklemlerle yapılır)
steps = int(distance / (c * planck_time))

for step in range(steps):
    elapsed += planck_time
    # (Burada enerji, faz, dalga fonksiyonu gibi parametreler ilerletilebilir)
    if step % (steps // 10 + 1) == 0:
        print(f"⏱️  Geçen Planck zamanı: {elapsed:.2e} s")

print(f"\n✅ Foton {distance} metreyi {elapsed:.3e} saniyede geçti.")
