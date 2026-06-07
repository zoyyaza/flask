from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      namaDepan = request.form['namaDepan']
      namaBelakang = request.form['namaBelakang']
      nama = f"{namaDepan} {namaBelakang}"
      
      hasil = ""
      for huruf in nama:
          if huruf.isupper():
              hasil += chr((ord(huruf) - 65 + 3) % 26 + 65)
          elif huruf.islower():
              hasil += chr((ord(huruf) - 97 + 3) % 26 + 97)
          else:
              hasil += huruf
          
      return render_template('response.html', nama_asli=nama, nama_terenkripsi=hasil)
      
   return render_template('form.html')

if __name__ == '__main__':
   application.run(debug=True)
