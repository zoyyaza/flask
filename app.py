from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        namaDepan = request.form.get('namaDepan', '')
        namaBelakang = request.form.get('namaBelakang', '')
        
        if namaDepan and namaBelakang:
            nama = f"{namaDepan} {namaBelakang}"
            
            # Caesar Cipher yang benar
            hasil = ""
            k = 3
            for char in nama:
                if char.isupper():
                    hasil += chr((ord(char) + k - 65) % 26 + 65)
                elif char.islower():
                    hasil += chr((ord(char) + k - 97) % 26 + 97)
                else:
                    hasil += char
            
            return render_template('response.html', 
                                 nama_asli=nama, 
                                 nama_terenkripsi=hasil)
    
    return render_template('form.html')

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port=5000)
