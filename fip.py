import requests
import time

# renvoie un dictionnaire avec les infos principales du morceau courant
def courant():
	r = requests.get("https://www.fip.fr/livemeta/7")
	musiques = r.json()['steps']
	for musique in musiques:
		debut = musiques[musique]['start']
		fin = musiques[musique]['end']
		horloge = time.time() #+ 70
		if(horloge>debut and horloge<fin):
			titre = musiques[musique]['title']
			auteurs = musiques[musique]['authors']
			album = musiques[musique]['titreAlbum']
			pochette = musiques[musique]['visual']
			return({'titre':titre,'auteurs':auteurs,'album':album,'pochette':pochette})

