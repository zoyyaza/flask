from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        namaDepan = request.form.get('namaDepan', '')
        namaBelakang = request.form.get('namaBelakang', '')
        
        if namaDepan and namaBelakang:
            nama_lengkap = f"{namaDepan} {namaBelakang}"
            hasil_enkripsi = caesar_encrypt(nama_lengkap, 3)
            
            # Cetak di terminal untuk debugging
            print(f"==================")
            print(f"Nama Depan: {namaDepan}")
            print(f"Nama Belakang: {namaBelakang}")
            print(f"Nama Lengkap: {nama_lengkap}")
            print(f"Hasil Enkripsi: {hasil_enkripsi}")
            print(f"==================")
            
            return render_template('response.html', 
                                 nama_asli=nama_lengkap, 
                                 hasil_enkripsi=hasil_enkripsi)
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
