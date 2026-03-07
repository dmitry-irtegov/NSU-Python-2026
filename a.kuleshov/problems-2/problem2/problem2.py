import unittest
from pathlib import Path
import textwrap

def convert_dictionary(file_path: str) -> Path:

    file_path = Path(file_path)
    lat_dict = {}

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue

            eng, latins = line.split("-")
            eng = eng.strip()

            for latin in latins.split(","):
                latin = latin.strip()
                lat_dict.setdefault(latin, []).append(eng)

    for latin in lat_dict:
        lat_dict[latin] = sorted(lat_dict[latin])

    lat_dict = dict(sorted(lat_dict.items()))

    output_path = file_path.with_name(file_path.stem + "_converted" + file_path.suffix)

    with open(output_path, "w", encoding="utf-8") as f:
        for latin, english_words in lat_dict.items():
            f.write(f"{latin} - {', '.join(english_words)}\n")

    return output_path

class TestDictionaryConversion(unittest.TestCase):

    input_file = "dict.txt"

    def test_full_dictionary_output(self):
        output_file = convert_dictionary(self.input_file)

        result = output_file.read_text(encoding="utf-8")

        expected_text = textwrap.dedent("""\
            adolescens - boy
            aedes - house
            aequitas - justice
            aevum - time
            alimentum - food
            alumnus - student
            amicus - friend
            amnis - river
            amor - love
            anima - life
            animal - animal
            aqua - water
            arbor - tree
            argentum - silver
            ars - art
            artificium - art
            astrum - star
            aura - wind
            aurum - gold
            avis - bird
            baca - fruit
            bacca - fruit
            bellator - soldier
            bellum - war
            bestia - animal
            caballus - horse
            caelum - sky
            camera - room
            canis - dog
            cantus - song
            carmen - song
            cattus - cat
            catulus - dog
            celeritas - speed
            chrysos - gold
            cibus - food
            cifra - number
            civitas - city
            cognitio - knowledge
            color - color
            concordia - peace
            crimen - crime
            cubiculum - room
            debilitas - weakness
            dies - day
            dilectio - love
            discipulus - student
            diurnum - day
            doctor - teacher
            doctrina - science
            domina - queen
            dominus - king
            domus - house
            electrum - silver
            epistula - letter
            equus - horse
            exemplum - example
            falsum - lie
            felis - cat
            femina - woman
            fiducia - hope
            figura - shape
            firmamentum - sky
            flamma - fire
            flora - flower
            flos - flower
            flumen - river
            forma - shape
            fortitudo - strength
            forum - market
            frater - brother
            genetrix - mother
            genitor - father
            germana - sister
            germanus - brother
            gramen - grass
            hal - salt
            harmonia - music
            helius - sun
            herba - grass
            homo - man
            hostis - enemy
            humus - earth
            ianua - door
            ichthys - fish
            ignis - fire
            infans - child
            infirmitas - weakness
            inimicitia - hate
            inimicus - enemy
            iocus - game
            iter - road, travel
            iugum - mountain
            ius - law
            iustitia - justice
            labor - work
            lac - milk
            lactis - milk
            lapis - stone
            letum - death
            lex - law
            liber - book
            lignum - tree
            lingua - language
            littera - letter
            ludus - game
            lumen - light
            luna - moon
            lux - light
            magister - teacher
            malum - apple, punishment
            mare - sea
            mater - mother
            mendacium - lie
            mercatus - market
            merum - wine
            metus - fear
            miles - soldier
            mons - mountain
            mors - death
            mulier - woman
            multa - punishment
            mundus - world
            musica - music
            navigium - ship
            navis - ship
            nemus - forest
            noctis - night
            nox - night
            numerus - number
            nummus - money
            obscuritas - darkness
            odium - hate
            opus - work
            orbis - world
            otium - rest
            pagus - village
            panis - bread
            pater - father
            pax - peace
            pecunia - money
            pelagus - sea
            peregrinatio - travel
            piscis - fish
            placenta - bread
            pomum - apple
            pons - bridge
            pontis - bridge
            popula - apple
            popum - fruit
            porta - door
            potentia - power
            puella - girl
            puer - boy, child
            pugna - war
            pulchritudo - beauty
            quies - rest
            regina - queen
            regio - country
            rex - king
            robur - strength
            sal - salt
            sapientia - knowledge
            saxum - stone
            scelus - crime
            scientia - science
            selene - moon
            sermo - language
            silentium - silence
            silva - forest
            sodalis - friend
            sol - sun
            sonus - sound
            soror - sister
            specimen - example
            spes - hope
            stella - star
            taciturnitas - silence
            tempus - time
            tenebrae - darkness
            terra - country, earth
            timor - fear
            tinctura - color
            unda - water
            urbs - city
            velocitas - speed
            ventus - wind
            venustas - beauty
            verbum - word
            veritas - truth
            verum - truth
            via - road
            vicus - village
            vinum - wine
            vir - man
            virgo - girl
            vis - power
            vita - life
            vocabulum - word
            volucris - bird
            volumen - book
            vox - sound
        """)

        self.assertEqual(result, expected_text)

    def test_output_file_name(self):
        output_file = convert_dictionary(self.input_file)
        self.assertEqual(output_file.name, "dict_converted.txt")

    @classmethod
    def tearDownClass(cls):
        output_file = Path("dict_converted.txt")
        if output_file.exists():
            output_file.unlink()


if __name__ == "__main__":
    unittest.main()