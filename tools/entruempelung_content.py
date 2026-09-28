# -*- coding: utf-8 -*-
"""
Inhalte des Bereichs „Entrümpelung“ (mdservicetrans.de/entruempelung/).

Mini-Markup in Texten:  **fett**   [Linktext](url)
Abschnittstypen (kind): text, bullets, checklist, steps, callout, prices
"""

DOMAIN = "https://www.mdservicetrans.de"
REGIONS = ["Nürnberg", "Fürth", "Erlangen", "Würzburg", "Schweinfurt", "Bamberg", "Bayreuth", "Ansbach"]

HUB = {
    "title": "Entrümpelung & Haushaltsauflösung Nürnberg & Franken | MD Service Trans",
    "description": "Entrümpelung, Haushaltsauflösung und Wohnungsräumung in Nürnberg & Franken: Räumen, fachgerecht Entsorgen, besenrein übergeben. Jetzt unverbindlich anfragen.",
    "h1": "Entrümpelung & Haushaltsauflösung in Nürnberg & Franken",
    "intro": "Wir räumen Wohnungen, Häuser, Keller, Dachböden, Garagen und Gewerberäume, entsorgen fachgerecht und übergeben die Räume besenrein. Vor dem Start erhalten Sie ein klares Angebot — nach Besichtigung oder anhand Ihrer Fotos.",
    "sections": [
        {
            "kind": "text",
            "h2": "Entrümpelung, Haushaltsauflösung, Wohnungsauflösung — was ist der Unterschied?",
            "paras": [
                "Die Begriffe werden im Alltag oft vermischt. Für die Planung lohnt sich ein genauer Blick, weil sich Umfang und Aufwand unterscheiden:",
            ],
        },
        {
            "kind": "prices",  # (Begriff, Erklärung)-Liste
            "items": [
                ("Entrümpelung", "Gegenstände und Gerümpel werden aus einzelnen Räumen oder Bereichen entfernt — etwa aus Keller, Dachboden oder Garage. Der Haushalt bleibt bestehen."),
                ("Haushaltsauflösung", "Ein kompletter Haushalt wird aufgelöst: Möbel, Hausrat und persönliche Dinge werden sortiert, verwertet oder entsorgt. Typisch nach einem Todesfall oder beim Umzug ins Pflegeheim."),
                ("Wohnungsauflösung / Wohnungsräumung", "Die Wohnung wird leer und besenrein übergeben — oft an Vermieter, Käufer oder Handwerker. Der Begriff wird häufig gleichbedeutend mit Haushaltsauflösung verwendet."),
                ("Vermüllte Wohnung", "Ein Sonderfall mit erhöhtem Aufwand, Schutzausrüstung und besonderer Diskretion."),
                ("Büro- & Geschäftsauflösung", "Räumung von Gewerbeflächen: Büros, Praxen, Läden, Werkstätten und Lager."),
            ],
        },
    ],
    "audience_h2": "Für wen wir räumen",
    "audience": [
        ("Erben & Angehörige", "Bei Todesfall oder Nachlass — mit Zeit zum Sortieren und Rücksprache."),
        ("Betreuer & Bevollmächtigte", "Wenn Wohnung oder Haus für eine andere Person aufgelöst wird."),
        ("Vermieter & Hausverwaltungen", "Wenn Räume für die Neuvermietung leer sein müssen."),
        ("Eigentümer & Verkäufer", "Vor Verkauf, Sanierung oder Umbau einer Immobilie."),
        ("Gewerbe", "Bei Betriebsaufgabe, Standortwechsel oder Neuausstattung."),
    ],
    "faq": [
        ("Was kostet eine Entrümpelung oder Haushaltsauflösung?",
         "Der Preis hängt vor allem von Menge, Stockwerk, Zugang und Art der Abfälle ab. Einen verbindlichen Preis nennen wir nach einer Besichtigung oder anhand Ihrer Fotos. Pauschalen ohne Kenntnis der Räume sind kaum belastbar."),
        ("Wie läuft eine Räumung bei Ihnen ab?",
         "Sie schildern uns die Situation, wir schätzen den Aufwand ein und erstellen ein klares Angebot. Nach Ihrer Zusage räumen wir zum vereinbarten Termin, entsorgen fachgerecht und übergeben die Räume besenrein."),
        ("Muss ich bei der Räumung anwesend sein?",
         "Nicht unbedingt. Nach Absprache können wir zum Beispiel mit einer Vertrauensperson vor Ort arbeiten oder die Schlüsselübergabe organisieren. Wichtig ist, dass vorab geklärt ist, was bleiben und was entsorgt werden soll."),
        ("Nehmen Sie auch Sperrmüll, Elektrogeräte und Schadstoffe mit?",
         "Sperrmüll und Elektrogeräte gehören zu einer Räumung dazu. Schadstoffhaltige Abfälle wie Farben, Lacke oder Chemikalien unterliegen besonderen Vorschriften — bitte nennen Sie uns solche Stoffe vorab, damit wir die Entsorgung korrekt planen können."),
        ("Was ist, wenn nur ein Teil geräumt werden soll?",
         "Das ist kein Problem. Sie legen fest, was bleibt und was entsorgt wird — wir räumen nur den vereinbarten Umfang."),
        ("In welchen Orten sind Sie im Einsatz?",
         "In Nürnberg und ganz Franken, zum Beispiel in Fürth, Erlangen, Würzburg, Schweinfurt, Bamberg, Bayreuth und Ansbach. Ihr Ort fehlt? Fragen Sie einfach an."),
    ],
}

PRICE_FACTORS = [
    ("Menge & Volumen", "Wie viele Räume und wie viel Hausrat oder Abfall zu räumen sind."),
    ("Stockwerk & Aufzug", "Tragewege und Treppen beeinflussen den Zeitaufwand."),
    ("Zugang & Parkmöglichkeit", "Enge Zugänge oder fehlende Stellplätze machen die Räumung aufwendiger."),
    ("Art des Abfalls", "Sperrmüll, Elektrogeräte und schadstoffhaltige Abfälle werden unterschiedlich entsorgt."),
    ("Verwertbare Gegenstände", "Gut erhaltene Dinge können nach Absprache berücksichtigt werden."),
    ("Zeitrahmen & Zusatzleistungen", "Sehr kurzfristige Termine oder Zusatzleistungen wie Demontage müssen gesondert geplant werden."),
]

SERVICES = [
    # ---------------------------------------------------------------- Haushaltsauflösung
    {
        "slug": "haushaltsaufloesung",
        "name": "Haushaltsauflösung",
        "icon": "home",
        "card": "Komplette Auflösung nach Todesfall, Umzug ins Pflegeheim oder Immobilienverkauf — diskret und mit Respekt vor dem Hausrat.",
        "title": "Haushaltsauflösung Nürnberg & Franken | MD Service Trans",
        "description": "Haushaltsauflösung in Nürnberg & Franken: Sortieren, Räumen und fachgerechte Entsorgung — diskret und zuverlässig. Jetzt unverbindlich anfragen.",
        "h1": "Haushaltsauflösung in Nürnberg & Franken",
        "intro": "Eine Haushaltsauflösung ist meist mehr als reine Logistik: Oft steckt ein Todesfall, ein Umzug ins Pflegeheim oder der Verkauf einer Immobilie dahinter. Wir übernehmen das Räumen, Sortieren und Entsorgen — diskret, nachvollziehbar und mit Respekt vor dem, was Ihnen wichtig ist. Vor dem Start erhalten Sie ein klares Angebot.",
        "includes": [
            "Besichtigung oder Einschätzung anhand Ihrer Fotos, danach ein klares Angebot",
            "Ausräumen aller Räume inklusive Keller, Dachboden, Garage und Nebengebäuden",
            "Sortieren in Erinnerungsstücke bzw. Wertvolles, Wiederverwertbares und Abfall — in Absprache mit Ihnen",
            "Fachgerechte Entsorgung; verwertbare Gegenstände nach Möglichkeit weiterverwenden",
            "Abstimmung mit Angehörigen, Nachlassverwaltern, Betreuern oder Hausverwaltungen",
            "Besenreine Übergabe der Räume",
        ],
        "when": [
            "Nach einem Todesfall",
            "Beim Umzug ins Pflegeheim, in betreutes Wohnen oder zu Angehörigen",
            "Vor Verkauf, Vermietung oder Erbauseinandersetzung einer Immobilie",
            "Bei Auswanderung, längerem Auslandsaufenthalt oder Trennung",
        ],
        "sections": [
            {
                "kind": "steps",
                "h2": "So läuft eine Haushaltsauflösung bei uns ab",
                "items": [
                    ("Anfrage", "Per Telefon, WhatsApp, E-Mail oder Formular — gern mit Fotos aller Räume, auch von Keller und Dachboden."),
                    ("Besichtigung oder Foto-Einschätzung", "Wir klären Umfang, Zugang, Stockwerk und Besonderheiten."),
                    ("Angebot", "Sie erhalten Leistungsumfang und Preis, bevor Kosten entstehen."),
                    ("Abstimmung", "Wir klären gemeinsam, was bleibt, was abgeholt und was entsorgt wird. Wichtige Unterlagen und Wertsachen werden vorab gesichert (siehe Checkliste)."),
                    ("Räumung & Sortierung", "Am vereinbarten Termin räumen wir die Räume aus und sortieren nach Absprache."),
                    ("Entsorgung & Übergabe", "Wir entsorgen fachgerecht und übergeben die Räume besenrein."),
                ],
            },
            {
                "kind": "checklist",
                "h2": "Checkliste: Das sollte vor der Räumung geklärt sein",
                "items": [
                    "**Wer darf beauftragen?** Eigentümer, Erbe bzw. Erbengemeinschaft (bei mehreren Erben in der Regel gemeinsam), Betreuer oder Bevollmächtigte mit Vollmacht, Nachlasspfleger oder eine Hausverwaltung im Auftrag des Eigentümers.",
                    "**Wichtige Unterlagen sichern:** Testament, Erbschein, Ausweise und Urkunden, Versicherungs-, Bank-, Renten- und Steuerunterlagen, Mietvertrag, Fahrzeugpapiere.",
                    "**Wertsachen getrennt sichern:** Schmuck, Bargeld, Münzen, Uhren, Kunst und Sammlungen.",
                    "**Erinnerungsstücke festlegen:** Fotoalben, Briefe und Familienstücke — Angehörige entscheiden am besten vorab.",
                    "**Schlüssel und Zugang:** alle Schlüssel (auch Keller, Dachboden, Garage, Briefkasten) und eine Parkmöglichkeit vor dem Haus.",
                    "**Mietwohnung:** Kündigung und Übergabetermin frühzeitig mit dem Vermieter abstimmen.",
                ],
            },
            {
                "kind": "callout",
                "title": "Hinweis zu Erbe und Mietvertrag (keine Rechtsberatung)",
                "paras": [
                    "Wer als Erbe in Betracht kommt, kann die Erbschaft in der Regel innerhalb von **sechs Wochen** ab Kenntnis ausschlagen. Wird der Nachlass vorher verwertet oder verkauft, kann das als Annahme der Erbschaft gewertet werden. Sind Sie unsicher, ob Sie das Erbe annehmen möchten, holen Sie vor einer Räumung oder Verwertung Rat beim Nachlassgericht, einem Notar oder Rechtsanwalt ein.",
                    "War die verstorbene Person Mieter, können Erbe und Vermieter das Mietverhältnis in der Regel **innerhalb eines Monats** nach Kenntnis vom Tod außerordentlich mit der gesetzlichen Frist kündigen. Klären Sie Fristen und Übergabetermin deshalb früh mit dem Vermieter — im Zweifel lassen Sie sich beraten.",
                ],
            },
            {
                "kind": "text",
                "h2": "Sortieren, Entsorgen, Verwerten",
                "paras": [
                    "Bei einer Haushaltsauflösung wird nicht einfach alles weggeworfen. Wir sortieren nach Absprache und trennen die Abfälle nach Art:",
                ],
            },
            {
                "kind": "bullets",
                "items": [
                    "Sperrmüll, Möbel und Matratzen",
                    "Elektro- und Elektronikgeräte — getrennt, nach den Vorgaben des Elektro- und Elektronikgerätegesetzes",
                    "Altholz, Metall, Textilien und Papier",
                    "Schadstoffhaltige Abfälle wie Farben, Lacke, Chemikalien und Batterien — bitte vorab nennen",
                    "Gut erhaltene Möbel und Hausrat: nach Absprache weitergeben oder verwerten; ob und wie sich das auf den Preis auswirkt, klären wir im Angebot",
                ],
            },
            {
                "kind": "prices",
                "h2": "Was beeinflusst den Preis einer Haushaltsauflösung?",
                "items": [
                    ("Menge & Volumen", "Zahl der Räume und Menge an Hausrat, Möbeln und Abfall."),
                    ("Stockwerk & Aufzug", "Tragewege und Treppen kosten Zeit."),
                    ("Zugang & Parken", "Enge Zugänge oder fehlende Stellplätze machen die Räumung aufwendiger."),
                    ("Art der Abfälle", "Sperrmüll, Elektrogeräte und schadstoffhaltige Stoffe werden unterschiedlich entsorgt."),
                    ("Verwertbares", "Gut erhaltene Gegenstände können nach Absprache berücksichtigt werden."),
                    ("Zeitrahmen & Zusatzleistungen", "Kurzfristige Termine oder z. B. der Abbau von Möbeln und Küchen."),
                ],
                "after": "Deshalb nennen wir einen verbindlichen Preis erst nach einer Besichtigung oder anhand Ihrer Fotos. Pauschalpreise „pro Zimmer“ ohne Kenntnis der Räume sind kaum belastbar.",
            },
            {
                "kind": "text",
                "h2": "Wie diskret arbeiten wir?",
                "paras": [
                    "Eine Haushaltsauflösung berührt oft private Lebensbereiche. Wir behandeln Ihre Anfrage und alles, was wir in den Räumen sehen, vertraulich, sprechen nicht mit Dritten darüber und gehen respektvoll mit Eigentum und Erinnerungsstücken um. Auf Wunsch stimmen wir uns direkt mit Angehörigen, Betreuern oder der Hausverwaltung ab.",
                ],
            },
        ],
        "faq": [
            ("Was kostet eine Haushaltsauflösung?",
             "Das hängt von Umfang, Stockwerk, Zugang und Art der Abfälle ab. Einen verbindlichen Preis nennen wir nach Besichtigung oder anhand Ihrer Fotos — Sie erfahren ihn, bevor Kosten entstehen."),
            ("Muss ich bei der Besichtigung oder der Räumung selbst dabei sein?",
             "Nicht zwingend. Nach Absprache können wir uns die Räume anhand von Fotos ansehen oder mit einer Vertrauensperson vor Ort abstimmen. Wichtig ist, dass wir wissen, was bleiben und was entsorgt werden soll."),
            ("Wer darf eine Haushaltsauflösung beauftragen?",
             "Der Eigentümer, der Erbe bzw. die Erbengemeinschaft, ein Betreuer oder Bevollmächtigter mit Vollmacht, ein Nachlasspfleger oder eine Hausverwaltung im Auftrag des Eigentümers. Bei mehreren Erben stimmen diese sich in der Regel gemeinsam ab."),
            ("Was passiert mit Wertgegenständen und Erinnerungsstücken?",
             "Sie legen vorab fest, was Sie behalten möchten. Wertsachen und persönliche Erinnerungsstücke sichern wir auf Wunsch getrennt, bevor die Räumung beginnt."),
            ("Was ist, wenn die Erbfolge noch nicht geklärt ist?",
             "Dann sollten Sie vor einer Räumung oder Verwertung rechtlichen Rat einholen (Nachlassgericht, Notar, Rechtsanwalt), denn eine Verwertung des Nachlasses kann Folgen für die Annahme oder Ausschlagung der Erbschaft haben. Wir räumen nur mit Ihrer Berechtigung zur Beauftragung."),
            ("Wie schnell kann die Haushaltsauflösung erfolgen?",
             "Das hängt von Umfang und aktueller Terminlage ab. Schildern Sie uns Ihre Situation und Ihren Wunschtermin — wir melden uns zeitnah mit einer realistischen Einschätzung."),
            ("Können Sie die Wohnung danach auch reinigen oder renovieren?",
             "Wir übergeben besenrein. Endreinigung und Renovierung sind eigene Leistungen — fragen Sie bei Bedarf gern danach."),
            ("Kann ich nur einen Teil des Haushalts auflösen lassen?",
             "Ja. Sie legen den Umfang fest, zum Beispiel nur einzelne Räume oder nur Keller und Dachboden."),
        ],
    },
    # ---------------------------------------------------------------- Wohnungsauflösung
    {
        "slug": "wohnungsaufloesung",
        "name": "Wohnungsauflösung & Wohnungsräumung",
        "icon": "key",
        "card": "Wohnung besenrein übergeben — von der Räumung bis zur Entsorgung, z. B. vor Auszug, Verkauf oder Renovierung.",
        "title": "Wohnungsauflösung Nürnberg & Franken | MD Service Trans",
        "description": "Wohnungsauflösung und Wohnungsräumung in Nürnberg & Franken: Terminabsprache, saubere Abwicklung und besenreine Übergabe. Jetzt Angebot anfragen.",
        "h1": "Wohnungsauflösung & Wohnungsräumung in Nürnberg & Franken",
        "intro": "Die Wohnung soll leer, sauber und übergabebereit sein — oft unter Zeitdruck. Wir räumen Möbel, Hausrat und Sperrmüll aus und entsorgen alles fachgerecht, damit Ihre Wohnung pünktlich an Vermieter, Käufer oder Handwerker übergeben werden kann.",
        "includes": [
            "Räumen von Möbeln, Elektrogeräten, Hausrat und Sperrmüll",
            "Tragen aus jedem Stockwerk, auch ohne Aufzug",
            "Fachgerechte Entsorgung und, wo möglich, Verwertung",
            "Besenreine Übergabe der Wohnung",
            "Terminabsprache nach Ihrem Zeitplan, etwa passend zum Übergabetermin",
        ],
        "when": [
            "Auszug mit Übergabetermin an den Vermieter",
            "Verkauf oder Neuvermietung einer Wohnung",
            "Räumung vor Renovierung oder Sanierung",
        ],
        "sections": [
            {
                "kind": "text",
                "h2": "Besenrein, Endreinigung, Schönheitsreparaturen — was ist gemeint?",
                "paras": [
                    "Bei der Wohnungsübergabe kommt es oft zu Missverständnissen. **Besenrein** bedeutet: grob gereinigt, ohne Gegenstände und Müll in den Räumen. Eine **Endreinigung** geht weiter, und ob Sie zusätzlich **Schönheitsreparaturen** schulden, richtet sich nach Ihrem Mietvertrag.",
                    "Wir räumen und übergeben besenrein. Was der Vermieter darüber hinaus verlangen darf, sollten Sie anhand Ihres Mietvertrags prüfen — im Zweifel hilft ein Mieterverein oder Rechtsanwalt.",
                ],
            },
            {
                "kind": "checklist",
                "h2": "Vor der Übergabe an den Vermieter",
                "items": [
                    "Übergabetermin und Kündigungsfrist im Mietvertrag prüfen",
                    "Alle Schlüssel bereithalten (Wohnung, Keller, Briefkasten, Haustür)",
                    "Zählerstände für Strom, Wasser und Heizung notieren",
                    "Übergabeprotokoll gemeinsam mit dem Vermieter erstellen und Mängel dokumentieren",
                    "Gegenstände festlegen, die Sie behalten oder bewusst zurücklassen möchten (z. B. Einbauküche nach Absprache)",
                ],
            },
            {
                "kind": "text",
                "h2": "Was beeinflusst den Preis einer Wohnungsräumung?",
                "paras": [
                    "Entscheidend sind Menge und Volumen, Stockwerk und Aufzug, der Zugang zur Wohnung (Parkmöglichkeit, enge Treppenhäuser) sowie die Art der Abfälle. Einen verbindlichen Preis nennen wir nach Besichtigung oder anhand Ihrer Fotos — bitte geben Sie Stockwerk und Aufzug in der Anfrage an.",
                ],
            },
        ],
        "faq": [
            ("Was bedeutet besenrein?",
             "Besenrein heißt: grob gereinigt, ohne Gegenstände und Müll in den Räumen. Eine Grund- oder Endreinigung ist etwas anderes — sprechen Sie uns an, falls Sie diese zusätzlich benötigen."),
            ("Ist die Räumung auch ohne Aufzug im Obergeschoss möglich?",
             "Ja. Stockwerk und Aufzug sind aber ein Faktor bei der Preisberechnung — bitte geben Sie beides in der Anfrage an."),
            ("Was ist, wenn nicht alles entsorgt werden soll?",
             "Kein Problem. Sagen Sie uns bei der Besichtigung, was bleiben oder abgeholt werden soll, und wir räumen nur den Rest."),
            ("Können Sie kurz vor dem Übergabetermin räumen?",
             "Das hängt von der aktuellen Terminlage ab. Nennen Sie uns in der Anfrage Ihren Übergabetermin — wir melden uns zeitnah mit einer realistischen Einschätzung."),
        ],
    },
    # ---------------------------------------------------------------- Keller, Dachboden, Garage
    {
        "slug": "keller-dachboden-garage",
        "name": "Keller, Dachboden & Garage",
        "icon": "box",
        "card": "Über Jahre Angesammeltes aus Keller, Dachboden, Garage oder Schuppen ausräumen und fachgerecht entsorgen.",
        "title": "Kellerentrümpelung Nürnberg & Franken | MD Service Trans",
        "description": "Keller, Dachboden und Garage entrümpeln in Nürnberg & Franken: Abholung, fachgerechte Entsorgung und unverbindliche Preiseinschätzung.",
        "h1": "Keller, Dachboden & Garage entrümpeln in Nürnberg & Franken",
        "intro": "Im Laufe der Jahre sammelt sich im Keller, auf dem Dachboden oder in der Garage vieles an. Wir räumen diese Bereiche aus — auch wenn der Zugang eng oder der Weg weit ist — und entsorgen alles, was Sie nicht mehr brauchen.",
        "includes": [
            "Ausräumen von Keller, Dachboden, Garage, Schuppen und Lagerräumen",
            "Abtransport von Sperrmüll, Regalen, Altmöbeln und Kartons",
            "Trennung nach Restmüll, Altholz, Metall und Wertstoffen",
            "Hinweise zu Abfällen, die gesondert entsorgt werden müssen",
            "Besenreine Übergabe des geräumten Bereichs",
        ],
        "when": [
            "Platz schaffen im Keller oder auf dem Dachboden",
            "Garage für Auto oder Umbau freimachen",
            "Vor Hausverkauf oder Sanierung",
        ],
        "sections": [
            {
                "kind": "callout",
                "title": "Was nicht in die normale Entrümpelung gehört",
                "paras": [
                    "**Schadstoffhaltige Abfälle** wie Farben, Lacke, Öle, Chemikalien, Batterien oder Gasflaschen unterliegen besonderen Vorschriften. Bitte nennen Sie uns solche Stoffe vorab.",
                    "**Bei Verdacht auf Asbest** (zum Beispiel alte Wellplatten, Bodenplatten oder Rohrisolierungen) fassen Sie die Materialien bitte nicht an. Ausbau und Entsorgung erfordern spezialisierte Fachbetriebe.",
                ],
            },
            {
                "kind": "text",
                "h2": "So bereiten Sie sich vor",
                "paras": [
                    "Ein paar Fotos vom Bereich und besonders vom **Zugang** (Treppen, Türbreiten, Gänge) helfen uns, den Aufwand realistisch einzuschätzen. Legen Sie vorab fest, was bleiben soll, und sichern Sie Wertsachen und wichtige Unterlagen, die sich häufig in Kellern und Dachböden ansammeln.",
                ],
            },
        ],
        "faq": [
            ("Nehmen Sie auch Farben, Lacke oder Chemikalien mit?",
             "Schadstoffhaltige Abfälle unterliegen besonderen Vorschriften. Bitte nennen Sie uns solche Stoffe vorab in der Anfrage, damit wir die Entsorgung korrekt planen können."),
            ("Was, wenn der Zugang sehr eng ist?",
             "Das ist bei Kellern und Dachböden häufig der Fall. Ein paar Fotos vom Zugang helfen uns, den Aufwand realistisch einzuschätzen."),
            ("Kann ich nur einen Teil entrümpeln lassen?",
             "Ja. Sie legen fest, was bleibt und was entsorgt wird — wir räumen nur den vereinbarten Umfang."),
            ("Was mache ich bei Verdacht auf Asbest?",
             "Berühren Sie das Material nicht und sprechen Sie uns vorab an. Asbesthaltige Materialien dürfen nur von Fachbetrieben ausgebaut und entsorgt werden."),
        ],
    },
    # ---------------------------------------------------------------- Vermüllte Wohnung
    {
        "slug": "vermuellte-wohnung",
        "name": "Vermüllte Wohnung & Messie-Entrümpelung",
        "icon": "heart",
        "card": "Sensible Räumungen ohne Vorurteile: diskret, respektvoll und in einem Tempo, das zur Situation passt.",
        "title": "Messie-Wohnung räumen Nürnberg & Franken | MD Service Trans",
        "description": "Vermüllte Wohnung oder Messie-Wohnung räumen in Nürnberg & Franken: diskret, ohne Vorurteile und mit sauberer Abwicklung. Vertraulich anfragen.",
        "h1": "Vermüllte Wohnung & Messie-Entrümpelung in Nürnberg & Franken",
        "intro": "Eine stark vollgestellte oder vermüllte Wohnung ist für Betroffene und Angehörige eine große Belastung. Wir gehen ohne Vorurteile vor, behandeln Ihre Anfrage vertraulich und räumen in einem Tempo, das zur Situation passt.",
        "includes": [
            "Vertrauliche Besprechung des Vorgehens vorab",
            "Schrittweises oder komplettes Räumen nach Absprache",
            "Sortieren, um Wichtiges und Persönliches zu erhalten",
            "Fachgerechte Entsorgung des Abfalls",
            "Besenreine Übergabe, auf Wunsch Hinweise zur anschließenden Reinigung",
        ],
        "when": [
            "Angehörige möchten einer betroffenen Person helfen",
            "Vermieter oder Hausverwaltung fordern eine Räumung",
            "Vor Renovierung, Verkauf oder Neuvermietung",
        ],
        "sections": [
            {
                "kind": "text",
                "h2": "Vorgehen bei stark vermüllten Räumen",
                "paras": [
                    "Bei starker Vermüllung kommen oft Hygiene- und Sicherheitsfragen hinzu, etwa Schimmel, Ungeziefer oder verdorbene Lebensmittel. Wir arbeiten mit geeigneter Schutzausrüstung und planen die Räumung so, dass sie für alle Beteiligten machbar bleibt. Bei der Besichtigung besprechen wir den Umfang, das Tempo und die Frage, was auf jeden Fall erhalten werden soll.",
                    "Wenn Sie sich als Angehörige Sorgen um eine betroffene Person machen: Neben der Räumung können auch Beratungsstellen Ihrer Stadt oder der Sozialpsychiatrische Dienst unterstützen.",
                ],
            },
        ],
        "faq": [
            ("Wie diskret läuft das ab?",
             "Ihre Anfrage und die Situation vor Ort behandeln wir vertraulich. Wir sprechen nicht mit Dritten darüber und gehen respektvoll mit den Räumen und den Betroffenen um."),
            ("Sind Fotos für die Einschätzung nötig?",
             "Sie helfen, ersetzen aber keinen Termin. Bei stark vermüllten Räumen empfehlen wir eine Besichtigung, um Umfang und Vorgehen sicher zu klären."),
            ("Reinigen Sie danach auch die Wohnung?",
             "Wir übergeben besenrein. Eine gründliche Reinigung oder Desinfektion ist ein eigener Leistungsumfang — sprechen Sie uns an, wenn Sie dafür Unterstützung benötigen."),
        ],
    },
    # ---------------------------------------------------------------- Büro / Geschäft
    {
        "slug": "geschaeftsaufloesung",
        "name": "Büro- & Geschäftsauflösung",
        "icon": "building",
        "card": "Büros, Praxen, Läden und Lager räumen — planbar, zügig und mit fachgerechter Entsorgung von Möbeln und Technik.",
        "title": "Büroauflösung & Geschäftsauflösung Nürnberg & Franken | MD Service Trans",
        "description": "Büro- und Geschäftsauflösung in Nürnberg & Franken: Möbel, Technik und Lagerbestand räumen und fachgerecht entsorgen. Jetzt Angebot anfragen.",
        "h1": "Büro- & Geschäftsauflösung in Nürnberg & Franken",
        "intro": "Beim Umzug, bei einer Betriebsaufgabe oder vor einer Neuvermietung müssen Gewerberäume zügig und ordentlich geräumt werden. Wir übernehmen Büros, Praxen, Läden, Werkstätten und Lager und planen die Räumung so, dass Ihr Betrieb möglichst wenig gestört wird.",
        "includes": [
            "Räumen von Büromöbeln, Regalen, Theken und Einrichtung",
            "Abtransport von Lagerbestand, Kartonagen und Verpackungsmaterial",
            "Entsorgung von Elektro- und Bürotechnik nach den geltenden Vorgaben",
            "Terminplanung auch außerhalb der Geschäftszeiten nach Absprache",
            "Besenreine Übergabe an Vermieter oder Nachmieter",
        ],
        "when": [
            "Betriebsaufgabe oder Standortwechsel",
            "Ende eines Mietvertrags mit Rückbaupflicht",
            "Neuausstattung von Büro- oder Ladenflächen",
        ],
        "sections": [
            {
                "kind": "callout",
                "title": "Akten, Datenträger und Aufbewahrungsfristen",
                "paras": [
                    "Geschäftsunterlagen unterliegen **gesetzlichen Aufbewahrungsfristen** — werfen Sie Akten und Belege deshalb nicht vorschnell weg. Im Zweifel klärt Ihr Steuerberater, was noch aufbewahrt werden muss.",
                    "Datenschutzrelevante Unterlagen und Datenträger müssen sicher vernichtet werden. Sprechen Sie uns vorab darauf an, damit wir im Einzelfall klären, wie das abläuft.",
                ],
            },
            {
                "kind": "text",
                "h2": "Rückbau und Übergabe an den Vermieter",
                "paras": [
                    "Gewerbemietverträge enthalten häufig Regelungen zu Rückbau und Übergabezustand. Klären Sie vorab, welche Einbauten entfernt werden müssen und in welchem Zustand die Fläche übergeben werden soll — wir stimmen Räumung und Termin darauf ab.",
                ],
            },
        ],
        "faq": [
            ("Können Sie auch Datenträger und Akten entsorgen?",
             "Datenschutzrelevante Unterlagen und Datenträger müssen sicher vernichtet werden. Sprechen Sie uns vorab darauf an — wir klären, wie das im Einzelfall abläuft."),
            ("Ist eine Räumung am Wochenende oder abends möglich?",
             "Nach Absprache ja. Nennen Sie uns in der Anfrage Ihr Zeitfenster."),
            ("Erhalte ich einen Nachweis für die Entsorgung?",
             "Fragen Sie uns bitte bei der Angebotsanfrage danach — der Umfang der Dokumentation hängt von Art und Menge der Abfälle ab."),
        ],
    },
]
