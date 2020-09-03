% import model
% rebase('base.tpl', title='KamenŠkarjePapir')


    <h1>Kamen, Škarje, Papir</h1>

    <blockquote>
    Igramo proti računalniku. Na voljo imamo tri možnosti, torej Kamen, Škarje ali Papir 
    in izberemo eno izmed danih izbir. Računalnik bo ob istem času naključno izbral eno 
    izmed danih opcij. Ko izberemo dano možnost, pritisnemo 'Enter', da potrdimo našo
    izbiro. Ali smo zmagali ali izgubili to rundo proti računalniku nam bo beležilo nad
    našo izbrano možnost. Če pride do neodločenega izida runde, program ne bo zabeležil
    ne zmage in ne poraza, tako da se igra nadaljuje dalje.
    
    Paziti je treba, da vnesemo dane možnosti z veliko začetnico, saj v nasprotnem primeru
    se ne bo nič zgodilo, če bomo vnašali kar koli drugega. Torej z igro lahko nadaljujemo
    naprej.
    </blockquote>


    <blockquote>
    Cilj igre je premagati računalnik tri runde, da zmagaš celotno igro.
    </blockquote>


Zmage: <b>{{igra.koliko_zmag(None)}}</b>
Porazi: <b>{{igra.koliko_porazov(None)}}</b>


% if poskus == model.ZMAGA:

    <h1><img src="/img/Zmaga.png" alt="NEKI"/></h1>

    <form action="/igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>

% elif poskus == model.PORAZ:

    <h1><img src="/img/Poraz.jpg" alt="NEKI"/></h1>

    <form action="/igra/" method="post">
        <button type="submit">Nova igra</button>
    </form>

% else:

    <form action="/igra/{{id_igre}}/" method="POST">
        Izbira: <input type="text" name="izbira">
    </form>

% end