# SubDojo v2.0 🔍

[![Version](https://img.shields.io/badge/Version-2.0-blue.svg)](https://github.com/naciblc/subdojo/releases)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

**Advanced Subdomain Enumeration & Reconnaissance Tool**

SubDojo v2.0 is a comprehensive subdomain enumeration tool that combines multiple reconnaissance techniques to discover subdomains efficiently. Built with Python and Go tools integration, it provides both passive and active enumeration capabilities.

**What's New in v2.0:**
- Enhanced redirect handling (301/302 redirects)
- Improved DNS and port-based validation
- SecurityTrails and VirusTotal API integrations
- Better false negative reduction
- Community-driven improvements

![SubDojo Banner](https://i.imgur.com/0FKcsVa.png)

## ⚠️ Legal & Ethical Notice

**This tool is developed strictly for authorized security assessments and ethical hacking purposes. Always obtain proper authorization before scanning any domain. The developers are not responsible for any misuse of this tool.**

---

## 🚀 Features

### 🔍 **Multi-Source Enumeration**
- **Passive Sources**: Crt.sh, Wayback Machine, HackerTarget, SecurityTrails, VirusTotal
- **Active Tools**: Subfinder, Amass, Assetfinder
- **Custom DNS Resolution**: Enhanced with reliable DNS servers

### 🌐 **Web Port Scanning**
- **Standard Ports**: Common web ports (49 ports)
- **Extended Mode**: All web ports (93 ports)
- **Protocol Support**: HTTP/HTTPS detection
- **Status Code Analysis**: Response status tracking

### 📊 **Advanced Analysis**
- **DNS Resolution**: Multi-resolver DNS checking
- **HTTP/HTTPS Validation**: Live subdomain verification
- **Redirect Tracking**: Follow and analyze redirects
- **Threaded Processing**: High-performance concurrent scanning

### 🎯 **Output & Reporting**
- **Structured Output**: Organized by domain and tool
- **Live Subdomains**: Filtered and validated results
- **Detailed Logs**: Comprehensive scanning reports
- **Timestamp Tracking**: All results with timestamps

---

## 📋 Requirements

### System Requirements
- **Python**: 3.8 or higher
- **Go**: 1.19 or higher
- **Operating System**: Linux, macOS, Windows (WSL)

### Python Dependencies
```
colorama>=0.4.6
pyfiglet>=0.8.post1
requests>=2.31.0
dnspython>=2.4.2
urllib3>=2.0.7
tqdm>=4.66.1
PyYAML>=6.0.1
```

### Go Tools (Auto-installed)
- [assetfinder](https://github.com/tomnomnom/assetfinder) - Subdomain enumeration
- [subfinder](https://github.com/projectdiscovery/subfinder) - Fast subdomain discovery
- [amass](https://github.com/OWASP/Amass) - In-depth subdomain enumeration

---

## 🛠️ Installation

### Quick Setup
```bash
# Clone the repository
git clone https://github.com/naciblc/subdojo.git
cd subdojo

# Create and activate virtual environment
python3 -m venv subdojo_env
source subdojo_env/bin/activate  # On Windows: subdojo_env\Scripts\activate

# Run the setup script
python3 setup.py
```

### Manual Installation

#### 1. Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv subdojo_env

# Activate virtual environment
# On Linux/macOS:
source subdojo_env/bin/activate

# On Windows:
subdojo_env\Scripts\activate

# Verify activation (you should see (subdojo_env) in your prompt)
which python  # Should point to your venv
```

#### 2. Install Go
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install golang-go

# macOS
brew install go

# Windows
# Download from https://golang.org/dl/
```

#### 3. Install Python Dependencies
```bash
# Make sure your virtual environment is activated
pip3 install -r requirements.txt
```

#### 4. Install Go Tools
```bash
# Assetfinder
go install github.com/tomnomnom/assetfinder@latest

# Subfinder
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Amass
go install github.com/owasp-amass/amass/v3/...@master
```

#### 5. Configure PATH
Add Go bin directory to your PATH:
```bash
export PATH=$PATH:$(go env GOPATH)/bin
# Add to ~/.bashrc or ~/.zshrc for permanent setup
```

### Virtual Environment Management

#### Activating the Environment
```bash
# Linux/macOS
source subdojo_env/bin/activate

# Windows
subdojo_env\Scripts\activate
```

#### Deactivating the Environment
```bash
deactivate
```

#### Updating Dependencies
```bash
# Activate environment first
source subdojo_env/bin/activate

# Update pip
pip install --upgrade pip

# Update requirements
pip install -r requirements.txt --upgrade
```

#### Removing Virtual Environment
```bash
# Deactivate first
deactivate

# Remove the environment
rm -rf subdojo_env
```

---

## ⚙️ Configuration

### DNS Resolvers
The tool uses a custom `resolvers.txt` file for enhanced DNS resolution:

```bash
# Default resolvers.txt content
1.1.1.1
8.8.8.8
8.8.4.4
1.0.0.1
208.67.222.222
208.67.220.220
```

### API Keys (Optional)
For enhanced functionality, configure API keys in `config.yaml`:

```yaml
virustotal:
  api_key: "your_virustotal_api_key"

securitytrails:
  api_key: "your_securitytrails_api_key"
```

---

## 🎯 Usage

### Basic Usage
```bash
# Activate virtual environment first
source subdojo_env/bin/activate  # On Windows: subdojo_env\Scripts\activate

# Basic subdomain enumeration
python3 main.py -d example.com

# With web port scanning
python3 main.py -d example.com -ap
```

### Command Line Options
```bash
python3 main.py -h
```

| Option | Description |
|--------|-------------|
| `-d, --domain` | Target domain (required) |
| `-ap, --allwebportscan` | Enable extended web port scanning |

### Examples
```bash
# Activate environment
source subdojo_env/bin/activate

# Standard enumeration
python3 main.py -d google.com

# Full enumeration with extended port scanning
python3 main.py -d google.com -ap

# Test on authorized domain
python3 main.py -d authorized-domain.com
```

---

## 📁 Output Structure

```
output/
└── subdomain/
    └── example.com/
        ├── Crt.sh-example.com-2024.01.15-10:30:45.txt
        ├── SecurityTrails-example.com-2024.01.15-10:30:45.txt
        ├── Virustotal-example.com-2024.01.15-10:30:45.txt
        └── live_subdomains/
            ├── Live-example.com-2024.01.15-10:30:45.txt
            └── live-example.com-2024.01.15-10:30:45-nonstandard-ports.txt
```

### Output Files
- **Raw Results**: Individual tool outputs
- **Live Subdomains**: Validated and accessible subdomains
- **Port Scan Results**: Web services found on non-standard ports

---

## 🔧 Modules Overview

### Core Modules
- **`main.py`**: Main application entry point
- **`modules/check.py`**: DNS and HTTP validation
- **`modules/command.py`**: Go tool execution
- **`modules/webportscan.py`**: Web port scanning

### Enumeration Modules
- **`modules/crtsh.py`**: Certificate transparency logs
- **`modules/wayback.py`**: Wayback Machine archives
- **`modules/hacker_target.py`**: HackerTarget API
- **`modules/securitytrails.py`**: SecurityTrails API
- **`modules/virustotal.py`**: VirusTotal API

---

## 🚀 Performance Tips

### Optimize Scanning Speed
1. **Use Reliable DNS Servers**: Update `resolvers.txt` with fast DNS servers
2. **Configure API Keys**: Enable all data sources for better coverage
3. **Adjust Thread Count**: Modify `max_workers` in modules for your system
4. **Use Extended Mode**: Enable `-ap` flag for comprehensive port scanning

### Best Practices
- **Authorized Testing Only**: Always get permission before scanning
- **Rate Limiting**: Respect API rate limits
- **Resource Management**: Monitor system resources during scanning
- **Result Validation**: Always verify discovered subdomains

---

## 🐛 Troubleshooting

### Common Issues

#### Go Tools Not Found
```bash
# Check Go installation
go version

# Verify PATH
echo $PATH | grep go

# Reinstall tools
go install github.com/tomnomnom/assetfinder@latest
```

#### Python Dependencies
```bash
# Upgrade pip
pip3 install --upgrade pip

# Install dependencies
pip3 install -r requirements.txt
```

#### DNS Resolution Issues
```bash
# Check resolvers.txt
cat resolvers.txt

# Test DNS servers
nslookup google.com 8.8.8.8
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup
```bash
# Clone and setup
git clone https://github.com/naciblc/subdojo.git
cd subdojo
python3 setup.py

# Run tests
python3 -m pytest tests/
```

---V

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **ProjectDiscovery** for Subfinder
- **OWASP** for Amass
- **Tom Hudson** for Assetfinder
- **All contributors** and the security community

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/naciblc/subdojo/issues)
- **Security**: Report security issues privately

---

<div align="center">
  <strong>🔐 Legal & Ethical | Stay Safe! 🛡️</strong>
  <br>
  <em>Remember: Only use on authorized domains!</em>
</div>

---

# SubDojo 🔍 (Türkçe)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Go](https://img.shields.io/badge/Go-1.19+-blue.svg)](https://golang.org)

**Gelişmiş Alt Alan Adı Keşif ve Keşif Aracı**

SubDojo, çoklu keşif tekniklerini birleştirerek alt alan adlarını verimli bir şekilde keşfeden kapsamlı bir alt alan adı keşif aracıdır. Python ve Go ile geliştirilmiş olup, hem pasif hem de aktif keşif yetenekleri sağlar.

![SubDojo Banner](https://i.imgur.com/0FKcsVa.png)

## ⚠️ Yasal ve Etik Uyarı

**Bu araç yalnızca yetkili güvenlik değerlendirmeleri ve etik hackleme amaçları için geliştirilmiştir. Herhangi bir alan adını taramadan önce mutlaka izin alın. Geliştiriciler bu aracın yanlış kullanımından sorumlu değildir.**

---

## 🚀 Özellikler

### 🔍 **Çok Kaynaklı Keşif**
- **Pasif Kaynaklar**: Crt.sh, Wayback Machine, HackerTarget, SecurityTrails, VirusTotal
- **Aktif Araçlar**: Subfinder, Amass, Assetfinder
- **Özel DNS Çözümleme**: Güvenilir DNS sunucuları ile geliştirilmiş

### 🌐 **Web Port Tarama**
- **Standart Portlar**: Yaygın web portları (49 port)
- **Genişletilmiş Mod**: Tüm web portları (93 port)
- **Protokol Desteği**: HTTP/HTTPS tespiti
- **Durum Kodu Analizi**: Yanıt durumu takibi

### 📊 **Gelişmiş Analiz**
- **DNS Çözümleme**: Çoklu resolver DNS kontrolü
- **HTTP/HTTPS Doğrulama**: Canlı alt alan adı doğrulama
- **Yönlendirme Takibi**: Yönlendirmeleri takip etme ve analiz etme
- **İş Parçacığı İşleme**: Yüksek performanslı eşzamanlı tarama

### 🎯 **Çıktı ve Raporlama**
- **Yapılandırılmış Çıktı**: Alan adı ve araç bazında organize edilmiş
- **Canlı Alt Alan Adları**: Filtrelenmiş ve doğrulanmış sonuçlar
- **Detaylı Günlükler**: Kapsamlı tarama raporları
- **Zaman Damgası Takibi**: Tüm sonuçlar zaman damgası ile

---

## 📋 Gereksinimler

### Sistem Gereksinimleri
- **Python**: 3.8 veya üzeri
- **Go**: 1.19 veya üzeri
- **İşletim Sistemi**: Linux, macOS, Windows (WSL)

### Python Bağımlılıkları
```
colorama>=0.4.6
pyfiglet>=0.8.post1
requests>=2.31.0
dnspython>=2.4.2
urllib3>=2.0.7
tqdm>=4.66.1
PyYAML>=6.0.1
```

### Go Araçları (Otomatik Kurulum)
- [assetfinder](https://github.com/tomnomnom/assetfinder) - Alt alan adı keşfi
- [subfinder](https://github.com/projectdiscovery/subfinder) - Hızlı alt alan adı keşfi
- [amass](https://github.com/OWASP/Amass) - Derinlemesine alt alan adı keşfi

---

## 🛠️ Kurulum

### Hızlı Kurulum
```bash
# Depoyu klonlayın
git clone https://github.com/naciblc/subdojo.git
cd subdojo

# Sanal ortam oluşturun ve etkinleştirin
python3 -m venv subdojo_env
source subdojo_env/bin/activate  # Windows'ta: subdojo_env\Scripts\activate

# Kurulum scriptini çalıştırın
python3 setup.py
```

### Manuel Kurulum

#### 1. Sanal Ortam Oluşturun
```bash
# Sanal ortam oluşturun
python3 -m venv subdojo_env

# Sanal ortamı etkinleştirin
# Linux/macOS'ta:
source subdojo_env/bin/activate

# Windows'ta:
subdojo_env\Scripts\activate

# Etkinleştirmeyi doğrulayın (prompt'unuzda (subdojo_env) görmelisiniz)
which python  # Sanal ortamınızı göstermeli
```

#### 2. Go Kurulumu
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install golang-go

# macOS
brew install go

# Windows
# https://golang.org/dl/ adresinden indirin
```

#### 3. Python Bağımlılıklarını Kurun
```bash
# Sanal ortamınızın etkin olduğundan emin olun
pip3 install -r requirements.txt
```

#### 4. Go Araçlarını Kurun
```bash
# Assetfinder
go install github.com/tomnomnom/assetfinder@latest

# Subfinder
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Amass
go install github.com/owasp-amass/amass/v3/...@master
```

#### 5. PATH Yapılandırması
Go bin dizinini PATH'inize ekleyin:
```bash
export PATH=$PATH:$(go env GOPATH)/bin
# Kalıcı kurulum için ~/.bashrc veya ~/.zshrc dosyasına ekleyin
```

### Sanal Ortam Yönetimi

#### Ortamı Etkinleştirme
```bash
# Linux/macOS
source subdojo_env/bin/activate

# Windows
subdojo_env\Scripts\activate
```

#### Ortamı Devre Dışı Bırakma
```bash
deactivate
```

#### Bağımlılıkları Güncelleme
```bash
# Önce ortamı etkinleştirin
source subdojo_env/bin/activate

# pip'i güncelleyin
pip install --upgrade pip

# Gereksinimleri güncelleyin
pip install -r requirements.txt --upgrade
```

#### Sanal Ortamı Kaldırma
```bash
# Önce devre dışı bırakın
deactivate

# Ortamı kaldırın
rm -rf subdojo_env
```

---

## ⚙️ Yapılandırma

### DNS Resolver'ları
Araç gelişmiş DNS çözümleme için özel `resolvers.txt` dosyası kullanır:

```bash
# Varsayılan resolvers.txt içeriği
1.1.1.1
8.8.8.8
8.8.4.4
1.0.0.1
208.67.222.222
208.67.220.220
```

### API Anahtarları (İsteğe Bağlı)
Gelişmiş işlevsellik için `config.yaml` dosyasında API anahtarlarını yapılandırın:

```yaml
virustotal:
  api_key: "virustotal_api_anahtarınız"

securitytrails:
  api_key: "securitytrails_api_anahtarınız"
```

---

## 🎯 Kullanım

### Temel Kullanım
```bash
# Önce sanal ortamı etkinleştirin
source subdojo_env/bin/activate  # Windows'ta: subdojo_env\Scripts\activate

# Temel alt alan adı keşfi
python3 main.py -d example.com

# Web port tarama ile
python3 main.py -d example.com -ap
```

### Komut Satırı Seçenekleri
```bash
python3 main.py -h
```

| Seçenek | Açıklama |
|---------|----------|
| `-d, --domain` | Hedef alan adı (gerekli) |
| `-ap, --allwebportscan` | Genişletilmiş web port taramayı etkinleştir |

### Örnekler
```bash
# Ortamı etkinleştirin
source subdojo_env/bin/activate

# Standart keşif
python3 main.py -d google.com

# Genişletilmiş port tarama ile tam keşif
python3 main.py -d google.com -ap

# Yetkili alan adında test
python3 main.py -d yetkili-alan-adi.com
```

---

## 📁 Çıktı Yapısı

```
output/
└── subdomain/
    └── example.com/
        ├── Crt.sh-example.com-2024.01.15-10:30:45.txt
        ├── SecurityTrails-example.com-2024.01.15-10:30:45.txt
        ├── Virustotal-example.com-2024.01.15-10:30:45.txt
        └── live_subdomains/
            ├── Live-example.com-2024.01.15-10:30:45.txt
            └── live-example.com-2024.01.15-10:30:45-nonstandard-ports.txt
```

### Çıktı Dosyaları
- **Ham Sonuçlar**: Bireysel araç çıktıları
- **Canlı Alt Alan Adları**: Doğrulanmış ve erişilebilir alt alan adları
- **Port Tarama Sonuçları**: Standart olmayan portlarda bulunan web servisleri

---

## 🔧 Modül Genel Bakış

### Çekirdek Modüller
- **`main.py`**: Ana uygulama giriş noktası
- **`modules/check.py`**: DNS ve HTTP doğrulama
- **`modules/command.py`**: Go araç yürütme
- **`modules/webportscan.py`**: Web port tarama

### Keşif Modülleri
- **`modules/crtsh.py`**: Sertifika şeffaflığı günlükleri
- **`modules/wayback.py`**: Wayback Machine arşivleri
- **`modules/hacker_target.py`**: HackerTarget API
- **`modules/securitytrails.py`
