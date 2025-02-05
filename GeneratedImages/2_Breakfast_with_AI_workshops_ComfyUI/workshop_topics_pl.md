# Zagadnienia

1. Sprzęt do uruchomienia ComfyUI
	1. **Zastosowania amatorskie.** ComfyUI może działać nawet na starszych kartach GeForce. Nie jest to sensowny pomysł, ale da się!
	2. **Istotne jest to, żeby nie dać się wciągnąć w symulator paska ładowania.** Długie czasy generowania obrazków nie sprzyjają eksperymentowaniu oraz tworzeniu nowych materiałów.
	3. **Zastosowania komercyjne oraz półprofesjonalne wymagają kart NVIDIA, najlepiej z rodziny RTX od wersji 30xx w górę.** Chodzi o zastosowaną architekturę - dopiero od tych kart firma wprowadziła rozwiązania wspierające generatywną sztuczną inteligencję.
	4. **Kluczowy jest VRAM, ale RAM-u też nie warto zaniedbywać.** Przy 8 GB VRAM da się pracować na niewielkich procesach, ale te bardziej rozbudowane wymagają już więcej pamięci - profesjonalnie trzeba mieć około 12 GB VRAM. Samego RAM-u przyjmuje się 32 GB jako normę. Dlaczego? Modele są najpierw ładowane do RAM-u, a potem na kartę graficzną. ComfyUI potrafi przerzucać modele między pamięciami, żeby odciążyć kartę, jeśli jakiś model nie jest już potrzebny.
	5. **Dominacja NVIDIA wynika z wykorzystania technologii Compute Unified Device Architecture.** Jest to sposób na ułatwienie pracy z kartą graficzną, dzięki czemu da się równolegle tworzyć różne fragmenty obrazka. Duże zadania są dzielone na mniejsze części i wykonywane równolegle.
	6. **CUDA nie występuje na Macach oraz kartach AMD.** W przypadku Maców czytałem o realizacjach, w których ComfyUI generowało obrazki w czasie krótszym niż 2 minuty, ale były to procesory M3 Max z dużą ilością RAM-u.
	7. **O kartę też trzeba dbać, szczególnie w przypadku pracy z generowaniem obrazków.** Utrzymywanie sensownej temperatury pozwala na mniejsze zużycie karty i sprawia, że będzie dłużej działać.
	8. **Przy przeliczaniu prac związanych z generowaniem grafiki należy brać pod uwagę różne kwestie** - od cen prądu po amortyzację sprzętu.

2. Skąd wziąć ComfyUI?
	1. **Najlepszym sposobem jest skorzystanie z oficjalnego [repozytorium](https://github.com/comfyanonymous/ComfyUI).** Wystarczy pobrać i rozpakować repozytorium.
	2. **Polecam zapoznać się też ze [Stability Matrix](https://github.com/LykosAI/StabilityMatrix).** To bardzo dobry interfejs, który ułatwia korzystanie z lokalnych narzędzi do generowania grafiki. Wiele rzeczy da się ogarnąć za pomocą jednego kliknięcia.
	3. **Co wybrać? ComfyUI czy SD Web UI?** To zależy od potrzeb. ComfyUI pozwala na dużą kontrolę nad procesem generowania obrazków - wręcz trzeba ten proces układać. Ma to swoje zalety. SD Web UI to prosty interfejs, gotowy do użycia zaraz po pobraniu modelu, ale jest bardzo rzadko aktualizowany.

3. Skąd brać modele?
	1. **Obecnie są dwa dobre miejsca, czyli [Hugging Face](https://huggingface.co/) oraz [CivitAI](https://civitai.com/).** Modele są przechowywane i tu, i tam - czasem jakiś model jest w jednym miejscu, a w innym go nie ma. Trzeba szukać.
	2. **Szczególną popularnością cieszy się CivitAI.** Jest nawet zintegrowane ze Stability Matrix - trzeba tam podać klucz API i łatwo można pobierać modele. 
	3. **Karta modelu, istotne informacje.** Przed pobraniem modelu konieczne jest sprawdzenie następujących rzeczy:
		1. **Jakiego rodzaju to jest model.** `Checkpoint` zawiera w sobie wszystko - pobieracie jeden plik i możecie działać. To oznacza, że w `checkpoint` jest już wrzucony CLIP, który odpowiada za interpretację promptu oraz VAE. 
		2. **Na podstawie jakiego modelu został wytrenowany model.** Kluczowe z perspektywy LoRA oraz sieci kontrolnych.
		3. **Jaka jest zalecana rozdzielczość.** Trzeba używać takiej, na jaką wskazują twórcy, w przeciwnym razie obrazki będą kiepskiej jakości.
		4. **Jakiego rodzaju promptu używa model.** To może być język naturalny lub tagi. Dodatkowo trzeba sprawdzić, czy wymaga promptu negatywnego. Sposób pisania promptu zależy od tego, w jaki sposób zostały opisane dane wykorzystane do trenowania modelu.
		5. **Jakich ustawień należy użyć, aby generować obrazki.** Dotyczy to samplera, a także tak zwanego `Clip Skip`. Jest to jeden z parametrów trenowania modeli, często ma wartość `2`, co oznacza, że przy interpretowaniu promptu przez model, model skupia się na ogólnej koncepcji, a nie na szczegółach. To nie jest zmienna, która poprawia jakość! Śrubki 10 nie odkręcicie kluczem 8.
		6. **Czy twórcy polecają używać konkretnego VAE.** VAE, czyli `Variational Auto Encoder`, odpowiada za wykonanie obrazka na podstawie abstrakcyjnej warstwy wygenerowanej w pamięci karty graficznej. Zdarza się, że w trakcie treningu modelu dochodzi do dużego skrzywienia VAE i wtedy twórcy polecają wykorzystywać VAE modelu podstawowego. 
		7. **Jaka jest licencja.** Tutaj życzę powodzenia, jeszcze jest Dziki Zachód. Na przykład niektóre modele są wytrenowane na obrazkach z popularnych filmów oraz serii anime. Można konkretną postać wywołać, używając określonej frazy w prompcie.
		8. **Jak należy skonfigurować sampler.** Sampler w ComfyUI odpowiada za generację obrazka, twórcy modeli często prezentują ustawienia pozwalające uzyskać najlepszą jakość.
	4. **Na CivitAI są też dostępne LoRY.** LoRA (`Low-Rank Adaptation`) to mały fragment modelu specjalnie wytrenowanego do skrzywiania uwagi większego modelu. LoRY wpływają na końcowy efekt pracy, dlatego są LoRY na ładne ręce, nogi lub konkretny sposób prezentacji. Użycie LoRY wymaga wykorzystania konkretnego słowa-klucza w prompcie!
	5. **Modele wrzuca się do konkretnego katalogu w ComfyUI.** Struktura jest samoopisująca się.

4. **ComfyUI Manager to doskonałe narzędzie do kontrolowania tego, jakie paczki ma się zainstalowane.** To powinno być domyślnie pobierane do ComfyUI - nie wyobrażam sobie pracy bez tego.
	1. **Znacznie ułatwia pracę z paczkami node'ów w ComfyUI.** Po prostu pobiera dane z repozytorium na GitHubie, rozpakowuje i instaluje. Rzuca też błędami!
	2. **W paczkach są node'y, które często wykonują te same funkcje, na dodatek mogą wchodzić w konflikty.** Jeśli używacie jakiegoś konkretnego node'a, to czasem trzeba pilnować, aby node'y z nim połączone były z tej samej paczki. O problemie użytkownik jest informowany, workflow się nie wykona.
	3. **Sami możecie też pisać node'y.** Ja to robiłem i robię, czyli sam jeszcze dorzucam swoje linijki kodu do tego bałaganu. Dobrze z pisaniem node'ów radzi sobie Claude, ale trzeba mu pomóc poprzez dorzucenie kilku wskazówek z dokumentacji.

5. **Opracowanie podstawowego workflow**
	1. **Do wygenerowania obrazka:** Checkpoint -> Prompt -> Sampler -> Obrazek.
	2. **Generowanie obrazka z użyciem sieci kontrolnych.** Wcześniej prezentacja jakie sieci kontrolne są dostępne i jak wyglądają ich efekty.
	3. **Elementy, które zostały wykorzystane w tworzonym workflow:**
		1. **Model:** [DreamSharperXL](https://civitai.com/models/112902/dreamshaper-xl)
		2. **LoRA:** [FLUX-style Lora for SDXL](https://civitai.com/models/625636?modelVersionId=700770)
		3. **Depth ControlNet:** [ControlNet SDXL](https://huggingface.co/ckpt/controlnet-sdxl-1.0/blob/main/control-lora-depth-rank256.safetensors)
		4. **Paczki:** [ComfyUI-Inspire-Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack), [ComfyUI-yanc](https://github.com/ALatentPlace/ComfyUI_yanc)

# Dodatkowe informacje

## Sprzęt, z którego korzystam

| W domu                                                       | W pracy (najsłabszy)                                           |  
| ------------------------------------------------------------ | -------------------------------------------------------------- | 
| i7 14700KF 3.4 GHz<br>64 GB RAM DDR5<br>RTX 4080 Super 16 GB | Ryzen 9 5950X 3.4 GHz<br>32 GB RAM DDR4<br>RTX 2070 Super 8 GB | 

## Przykłady promptów

| Język naturalny                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Tagi |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---- |
| A sophisticated urban loft interior bathed in deep cherry red lighting. The main focus is a plush burgundy velvet sofa with metallic chrome legs catching reflections from subtle neon art installations. The space features polished concrete floors contrasting with luxurious textiles, while dramatic shadows cast by modern sculptural lighting fixtures create pockets of intrigue. Shot in a cinematic style with emphasis on depth and dimension, resembling a high-end fashion editorial. The atmosphere is moody yet refined, with precise highlights accentuating the interplay between soft and hard surfaces throughout the contemporary space. | establishing shot, confident young woman portrait, dramatic graphic novel illustration with detailed crosshatching, intricate ink work and lineart, elegant pose on wooden chair, long flowing hair with styled bangs, graceful facial expression, ornate floral backdrop with organic patterns, high contrast black and white with midnight blue accents, soft rim lighting casting dramatic shadows, complex background details, warm gradients, style by Moebius, ligne claire technique, intricate 8K detail     |

## Modele do pokazania

[EpicRealism](https://civitai.com/models/277058?modelVersionId=1346244), [Pony](https://civitai.com/models/257749?modelVersionId=290640), [DreamShaper](https://civitai.com/models/4384?modelVersionId=128713), [Flux](https://civitai.com/models/618692?modelVersionId=691639).

## Diffusion Based Model

Modele *diffusion* generują zawartość w taki sposób, że usuwają niepotrzebny szum (*noise*). W każdym kroku z chaosu zaczynają wyciągać bardziej skonkretyzowany obrazek na podstawie użytego promptu. Link do [wideo](https://github.com/nathannlu/aperture).

## Sampler. Opis elementów

| Nazwa elementu                 | Opis                                                                                                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Seed                           | Liczba, która kontroluje wstępną losowość generacji obrazka.<br>Używanie tej samej gwarantuje podobne obrazki.                                                                                                |
| Steps                          | Liczba kroków, jakie podejmuje AI w tworzeniu obrazka.<br>Zazwyczaj jest tak, że im więcej kroków, tym lepszy obrazek.                                                                                          |
| CFG (Classifier Free Guidance) | Określa, jak bardzo model trzyma się promptu.<br>Im wyższa wartość, tym mocniej odwołuje się do promptu, ale to nie oznacza automatycznego skoku jakości!                                                      |
| Sampler Name                   | Algorytmy wykorzystywane w generowaniu obrazu.<br>**Euler**: Szybki, najczęściej używany. **DPM++**: wolniejszy, ale tworzy obrazy wyższej jakości. **DDIM**: Dobry, jeśli trzeba utrzymać spójność kompozycji |
| Scheduler                      | Kontroluje to, jak usuwany jest chaos z obrazka.<br>**Normal**: Standardowy, najczęściej wykorzystywany. **Karras**: Skupia się na detalach. **Linear**: Skupia się na zachowaniu spójności kompozycji.        |
| Denoise                        | Określa, ile oryginalnego obrazka jest zachowane przy generacji `image2image`                                                                                                                                                                                                             |
### Kobieta na moście

#### Prompt +

```
cinematic analog film still, masterpiece, best quality, portrait of an elegant woman standing on an ornate stone bridge, natural pose, casual elegant clothing, soft afternoon sunlight, historic European architecture, weathered stone textures, river below, film grain, muted vintage colors, Kodak Portra 400 style, depth of field, nostalgic atmosphere, intricate details, 8k, amazing quality
```

#### Prompt -

```
(low quality, worst quality:1.4), cgi, text, signature, watermark, extra limbs, ugly, deformed, noisy, blurry, low contrast, oversaturated, modern elements, digital looking, heavy grain, overexposed
```

### Pies na plaży

#### Prompt +

```
masterpiece, best quality, pastel art sketch, black dog standing majestically on sandy beach, soft ocean waves background, gentle morning light, fluffy fur details, serene expression, playful pose, coastal atmosphere, seabirds in sky, pastel color palette, soft artistic strokes, traditional media, watercolor paper texture, detailed fur rendering, amazing quality
```

#### Prompt -

```
(low quality, worst quality:1.4), cgi, text, signature, watermark, extra limbs, ugly, deformed, noisy, blurry, low contrast, photorealistic, digital art, harsh lines, anatomically incorrect, cartoon style, oversaturated colors
```