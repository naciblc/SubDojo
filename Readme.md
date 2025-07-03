# SubDojo

![SubDojo Logo](https://i.imgur.com/3QXk22N.png) 

**Ethical Note:** This tool is developed strictly for authorized security assessments and ethical hacking purposes. Always obtain proper authorization before scanning.

---

## Features
Performs detailed reconnaissance using:
- **Assetfinder**
- **Subfinder**  
- **Amass**  
- **Crt.sh**  
- **HackerTarget**  
- **Wayback Machine**

---

## Requirements

### Go Installation
- **Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install golang-go
```

- **macOS (Homebrew):**
```bash
brew install go
```
Verify: `go version`

---

## Required Tools
- [assetfinder](https://github.com/tomnomnom/assetfinder)
- [subfinder](https://github.com/projectdiscovery/subfinder)  
- [amass](https://github.com/OWASP/Amass)

---

## Installation
```bash
python3 setup.py
```
This will:
1. Check Go environment
2. Install required tools
3. Configure PATH if needed

---
## Enhanced DNS Resolution

For optimal subdomain discovery, we recommend using a custom `resolvers.txt` file containing reliable DNS servers.

### Setup Resolvers:
1. Create a `resolvers.txt` file in the main directory:
```bash
nano resolvers.txt
```

2. Add your preferred DNS servers (one per line):

# Public DNS
1.1.1.1
8.8.8.8

3. The tool will automatically use these resolvers for:
   - Faster DNS lookups
   - Bypassing local DNS restrictions
   - More comprehensive subdomain discovery

---
## Usage
```bash
python3 main.py -d example.com
```
`-d`: Target domain (use only authorized domains)

---

## Outputs
- Raw results: `SubDojo/output/subdomain/`
- Live subdomains: `.../live_subdomains/`

---


<div align="center">
  <strong>🔐 Legal & Ethical | Stay Safe! 🛡️</strong>
</div>

---

# SubDojo (Türkçe)

![SubDojo Logo](https://i.imgur.com/3QXk22N.png) 

**Etik Uyarı:** Bu araç yalnızca yetkili güvenlik testleri için geliştirilmiştir. Tarama yapmadan önce mutlaka izin alın.

---

## Özellikler
Şu araçlarla detaylı keşif yapar:
- **Assetfinder**
- **Subfinder**  
- **Amass**  
- **Crt.sh**  
- **HackerTarget**  
- **Wayback Machine**

---

## Gereksinimler

### Go Kurulumu
- **Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install golang-go
```

- **macOS (Homebrew):**
```bash
brew install go
```
Kontrol: `go version`

---

## Gerekli Araçlar
- [assetfinder](https://github.com/tomnomnom/assetfinder)
- [subfinder](https://github.com/projectdiscovery/subfinder)  
- [amass](https://github.com/OWASP/Amass)

---

## Kurulum
```bash
python3 setup.py
```
Bu işlem:
1. Go ortamını kontrol eder
2. Araçları kurar
3. Gerekirse PATH'i ayarlar

---
## Gelişmiş DNS Çözümleme

Daha kapsamlı subdomain keşfi için özel `resolvers.txt` dosyası kullanmanızı öneririz.

### Resolver Kurulumu:
1. Ana dizininde dosya oluşturun:
```bash
nano resolvers.txt
```

2. Tercih ettiğiniz DNS sunucularını ekleyin:
```text
# Genel DNS'ler
1.1.1.1
8.8.8.8

```

3. Araç bu resolver'ları otomatik kullanacaktır:
   - Daha hızlı sorgulama
   - Yerel DNS kısıtlamalarını aşma
   - Daha kapsamlı subdomain bulma

---

## Kullanım
```bash
python3 main.py -d example.com
```
`-d`: Hedef domain (sadece yetkili domainlerde kullanın)

---

## Çıktılar
- Ham sonuçlar: `SubDojo/output/subdomain/`
- Canlı subdomainler: `.../live_subdomains/`

---

<div align="center">
  <strong>🔐 Legal & Ethical | Stay Safe! 🛡️</strong>
</div>
