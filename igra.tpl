% import model
% rebase('base.tpl', title='KamenŠkarjePapir')


<h1>Kamen, Škarje, Papir</h1>

    <blockquote>
     besedilo
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