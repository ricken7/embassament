
5
 
3 
 
Agència Catalana de l’Aigua 
Manual d’ús del servei API-REST 
1 Propòsit del document 
L'Agencia Catalana de l'Aigua posa disposició de tercers tot un conjunt d'eines de consulta de 
dades  relacionades  amb  l'aigua  i  el  medi.  El  present  document  explica  la  implantació  de  la 
plataforma Sentilo com a eina per l'accés a la informació existent a l'ACA. Aquesta implantació 
s’anomena Sistema de Publicació de Dades en Temps Real. 
El projecte Sentilo ha estat impulsat i conceptualitzat per l'Ajuntament de Barcelona mitjançant 
la creació d'una plataforma que permet recollir, explotar i difondre la informació generada pels 
sensors desplegats en una ciutat o regió. Aquest projecte està sent ampliat per contribucions 
d'altres entitats i organismes públics enriquint la idea inicial amb noves funcionalitats, 
connectors o aplicacions relacionades. 
La plataforma Sentilo està desenvolupada íntegrament amb components de programari lliure 
perquè  qualsevol  organisme  la  pugui  utilitzar  directament  per  interconnectar  els  sensors  i 
actuadors que vagi desplegant. El programari lliure permet abaratir substancialment els costos 
d'implantació  de  les  infraestructures  de  les  Smart  Cities/Regions,  ja  que  no  cal  que  cada 
organisme desenvolupi la seva pròpia plataforma quan un altre ja ha fet aquesta inversió i en 
comparteix la solució. 
El  principal  objectiu  de  Sentilo  és  proporcionar  a  tots  els  organismes  que  ho  desitgin  una 
plataforma funcional, oberta, interoperable i fàcilment ampliable, compartint la inversió pública 
del desenvolupament amb el model de programari lliure. 
A continuació, s’expliquen les crides que les entitats terceres han de realitzar per accedir a la 
informació que l’ACA posa a disposició dintre del Sistema de Publicació de Dades en Temps 
Real.  Aquestes  crides  permeten  l’accés  a  la  llista  de  sensors  o  la  consulta  de  les  mesures 
enregistrades. 
  
 
4 
 
Agència Catalana de l’Aigua 
Manual d’ús del servei API-REST 
2 API per consultar sensors i 
mesures 
2.1 Mecanisme de crida 
El  Sistema  de  Publicació  de  Dades  en  Temps  Real  de  l’ACA  proporciona  una  API  REST, 
mitjançant la plataforma Sentilo, que permet la consulta de les dades. Per més informació: 
 https://ca.wikipedia.org/wiki/REST  
 http://www.sentilo.io/wordpress  
Per consultar sensors i mesures s’hauran de fer peticions HTTP GET. 
2.2 Autenticació i autorització 
El Sistema de Publicació de Dades disposa de la possibilitat de configurar l’accés a la informació 
mitjançant un mecanisme d’autorització i autentificació. En aquest cas, l’ACA proporciona una 
clau que és necessari utilitzar a qualsevol petició HTTP GET. 
L'autenticació  consisteix  en  enviar  en  qualsevol  petició  HTTP  una  capçalera  HTTP  de  nom 
IDENTITY_KEY i valor una cadena de caràcters que l'ACA proporcionarà a cada entitat tercera. 
L’accés públic no requereix la utilització de cap clau. 
2.3 Representació de les dades consultades 
Com a resultat de les peticions HTTP GET de consulta s’obtindrà la informació en representació 
JSON. 
Més informació: 
 https://ca.wikipedia.org/wiki/JSON  
  
 
5 
 
Agència Catalana de l’Aigua 
Manual d’ús del servei API-REST 
2.4 Consulta de la llista de sensors autoritzats 
2.4.1 Petició HTTP GET 
Per realitzar aquesta consulta s’utilitza la crida al catàleg amb la possibilitat de filtrar per tipus 
d’element, la URL a cridar es la següent: 
 http://aca-web.gencat.cat/sdim2/apirest/catalog  
 http://aca-web.gencat.cat/sdim2/apirest/catalog?componentType=embassament  
2.4.2 Exemple de resultat 
Com  a  resultat  s’obté  un  missatge  amb  representació  JSON  amb  el  llistat  dels  sensors 
autoritzats. Per a cadascun s’obté informació semblant a la següent: 
{ 
provider: " EMBASSAMENT-EST" 
permission: "READ" 
sensors: 
<...> 
{ 
sensor:"4115520" 
description: "Percentatge volum embassament" 
dataType: "NUMBER" 
location: " 41.255628749 1.6510102179199748" 
type: "0039" 
unit: "%" 
publicAccess: true 
component: " L08058-72-00003" 
componentType: "embassament" 
componentDesc: " Embassament de Foix" 
componentPublicAccess: true 
<...> 
} 
<...> 
} 
2.4.3 Explicació del missatge JSON 
Les informacions rellevants son les següents: 
 provider: Identificador del provider del que penja un sensor. Al sistema de publicació de 
dades de l’ACA tot sensor penja d’un provider. Al llistat anterior podria aparèixer més d’un 
provider, cadascun amb tots els sensors que pengen d’ell. És una dada rellevant ja que és 
 
6 
 
Agència Catalana de l’Aigua 
Manual d’ús del servei API-REST 
necessari  conèixer  el  provider  del  que  penja  un  sensor  per  poder  consultar  les  seves 
mesures. 
 sensor: Identificador de la variable (el concepte sensor i variable son equivalents). És una 
dada rellevant ja que és necessari conèixer aquest codi per poder consultar mesures de la 
variable. 
 description: Descripció de la variable. Pot no estar informat. 
 dataType: Tipus de dada. Les possibilitats són: NUMBER (numèric), TEXT (text), 
BOOLEAN (booleà). 
 location: Coordenades de geolocalització de l’estació a què pertany el sensor. Pot no estar 
informat. 
 type: Tipus de variable. 
 unit: Unitat de mesura de la variable. Pot no estar informat. 
 component: Codi de l’estació a què pertany la variable. 
 componentType: Tipus d’estació 
 componentDesc: Descripció de l’estació a què pertany la variable. Pot no estar informat. 
2.4.4 Recomanació sobre encauament del resultat 
 El Sistema de Publicació de Dades de l'ACA no retorna capçaleres d’encauament (cache) en 
la resposta HTTP resultant de la consulta de la llista de variables autoritzades. 
Això és perquè en qualsevol moment el resultat de la 
consulta  podria  canviar.  No  obstant,  cal  tenir  en 
compte per un costat que es tracta d'informació poc 
volàtil i, per l'altra, que el llistat retornat pot ser gran 
i,  per  tant,  trigar  alguns  segons  en  generar-se  i 
retornar-se. 
Si, per exemple, es volguessin recuperar les darreres 
mesures de totes les variables autoritzades, la 
manera correcta de fer-ho seria obtenir el llista 
anterior una única vegada per consultar la mesura de 
cadascun  dels  sensors.  No  s'hauria  de  obtenir  el 
llistat anterior tantes vegades com sensors hi hagi ja que això només engrandiria la durada del 
procés de consulta de les mesures. 
2.4.5 Sensors per a valors agregats de mesures 
Per a certes variables el Sistema de Publicació de Dades de l'ACA proporciona valors agregats 
a diferents nivells (horari, diari, setmanal, mensual i anual). 
A  l’apartat  2.5.4  “Valors  simples,  complexos  i  agregats”,  s'explica  la  diferencia  entre  valors 
sense  agregar,  que  expressen  una  mesura  presa  en  un  instant  concret  (per  exemple,  la 
S'aconsella que la 
entitat tercera 
desenvolupi algun tipus 
de mecanisme 
d’encauament del llistat 
obtingut durant cert 
temps. 
 
7 
 
Agència Catalana de l’Aigua 
Manual d’ús del servei API-REST 
temperatura  a  les  12:45  d'un  dia  concret),  i  agregats  (per  exemple,  la  temperatura  mitjana 
mesurada al llarg de tot un dia) 
Al llistat retornat per la consulta explicada abans és senzill identificar aquestes variables, ja que 
l’identificador  del  sensor  finalitza  amb  un  símbol  de  guió  baix  (_)  seguit  d'una  de  les  lletres 
següents: 
 H, per agregacions horàries 
 D, per agregacions diàries 
 S, per agregacions setmanals 
 M, per agregacions mensuals 
 A, per agregacions anuals 
2.5 Consulta de la darrera mesura d’un sensor 
autoritzat 
2.5.1 Petició HTTP GET 
Per realitzar aquesta consulta la entitat tercera ha de cridar a la URL següent: 
 http://aca-web.gencat.cat/sdim2/apirest/data/<provider>/<sensor>  
Per exemple: 
 http://aca-web.gencat.cat/sdim2/apirest/data/EMBASSAMENT-EST/083036-001-ANA023  
2.5.2 Exemple de resultat 
Com a resultat s'obté un missatge amb representació JSON amb la darrera mesura 
enregistrada per a la variable demanada en un format com el següent: 
{ 
observations: [ 
{ 
value: " 421.466" 
timestamp: " 06/02/2020T07:00:00" 
location: "" 
} 
] 
} 
 
8 
 
Agència Catalana de l’Aigua 
Manual d’ús del servei API-REST 
2.5.3 Explicació del missatge JSON 
Les informacions rellevants son les següents: 
 value: Valor de la mesura. Al següent apartat es detallen les diferents tipologies de valors.  
 timestamp: Instant en què s’ha pres la mesura en sistema horari UTC i format 
dd/mm/aaaaThh:mi:ss 
2.5.4 Explicació del missatge JSON 
Pel que fa a les mesures, el Sistema de Publicació de Dades de l'ACA proporciona: 
 Valors que poden ser simples (no estructurats) o complexos (estructurats): 
o Simples (no estructurats): en aquest cas el valor expressa un sol concepte: Per 
exemple, una temperatura, una profunditat, nivell d’embassament, etc. 
o Complexos (estructurats): en aquest cas el valor expressa més d'un concepte. 
 Valors que podran ser agregats (per un període de temps) o sense agregar: 
o Sense agregar, amb el valor mesurat en un moment concret. 
o Agregats (per un període de temps), amb el valor mitjà, màxim i mínim dins d'un 
interval  d'agregació  (horari,  diari,  setmanal...);  en  aquest  cas  timestamp  vindrà 
informat amb l'instant final de l'interval d'agregació. 
Exemples: 
 Mesura amb valor simple sense agregar: 
o http://aca-web.gencat.cat/sdim2/apirest/data/AFORAMENT-EST/CALC001244  
o Resultat: 
{ 
observations: [ 
{ 
value: "21.715" 
timestamp: "06/02/2020T07:35:00" 
location: "" 
} 
] 
} 
o Explicació:  Indicaria  un  cabal  de  21,715  m3/s  enregistrat  a  las  07:35:30  del  6  de 
febrer del 2020 a l’estació d’aforament de Castellbell i el Vilar (riu Llobregat). 
  
 
9 
 
Agència Catalana de l’Aigua 
Manual d’ús del servei API-REST 
 Mesura amb valor complex sense agregar: 
o http://aca-web.gencat.cat/sdim2/apirest/data/PLATGES-MDS/3984145  
o Resultat: 
{ 
observations: [ 
{ 
value: "{“presencia”:si, 
“mida”:petites, 
“perillositat”:alta}" 
timestamp: "08/06/2015T12:15:00" 
location: "" 
} 
] 
} 
o Explicació:  Indicaria  la  presencia  de  petites  meduses  perilloses  de  la  espècie 
“Pelagia  noctiluca  (Pn)”  a  las  12:45:30  del  8  de  juny  del  2015  a  la  platja  de  la 
Martinenca. 
 Mesura amb valor agregat: 
o http://aca-web.gencat.cat/sdim2/apirest/data/PLATGES-MAB/3984465_D  
Observar que l'identificador de la variable (sensor) finalitza amb guió baix (_) seguit 
de  una  lletra  “D”.  Tal  i  com  s'ha  explicat  abans  estem  consultant  l'agregació  d'un 
interval d'un dia. 
o Resultat: 
{ 
observations: [ 
{ 
value: "{“avg”:23.7, 
“max”:25.6, 
“min”:22.1}" 
timestamp: "23/08/2015Z23:59:59" 
location: "" 
} 
] 
} 
o Explicació: Indicaria que durant el dia 23 d'agost del 2015 la temperatura de l'aigua 
de  bany  a  la  platja  de  la  Martinenca  ha  sigut  de  23.7  ºC  de  mitjana,  25.6  ºC  de 
màxima i 22.1 ºC de mínima. 
  
 
10 
 
Agència Catalana de l’Aigua 
Manual d’ús del servei API-REST 
2.6 Consulta de les mesures d’un sensor 
autoritzat durant un interval de temps 
2.6.1 Petició HTTP GET 
Per  realitzar  aquesta  consulta  la  entitat  tercera  ha  de  cridar  a  la  URL  següent  enviant  en  la 
petició la capçalera HTTP IDENTITY_KEY esmentada abans: 
 http://aca-
web.gencat.cat/sdim2/apirest/data/<provider>/<sensor>?limit=<n>&from=<dd/mm/yyyyThh
:mi:ss>&to=<dd/mm/yyyyThh:mi:ss> 
On: 
 limit: indica fins a quantes mesures es volem recuperar. 
 from: indica l'instant inicial de l'interval de temps. 
 to: indica l'instant final de l'interval de temps. 
Per exemple: 
 http://aca-web.gencat.cat/sdim2/apirest/data/EMBASSAMENT-EST/083036-001-
ANA023?limit=7&from=14/01/2020T09:00:00&to=14/01/2020T12:00:00   
2.6.2 Exemple de resultat 
Com  a  resultat  s'obté  un  missatge  amb  representació  JSON  amb  un  llistat  de  mesures 
enregistrades per a la variable demanada en un format com el següent: 
{ 
observations: [ 
{ 
value: "412.87", 
timestamp: "14/01/2020T11:55:00", 
location: "" 
}, 
{ 
value: "412.87", 
timestamp: "14/01/2020T11:50:00", 
location: "" 
}, 
{ 
value: "412.87", 
