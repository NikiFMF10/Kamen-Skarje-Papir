% import model
% rebase('base.tpl', title='KamenŠkarjePapir')


<h1>Kamen, Škarje, Papir</h1>

    <blockquote>
     besedilo
    </blockquote>


Zmage: <b>{{igra.koliko_zmag(None)}}</b>
Porazi: <b>{{igra.koliko_porazov(None)}}</b>


% if poskus == model.ZMAGA:

    <h1> ZMAGA! <h1>

    <form action="/igra/" method="post">
        <button type="submit">Nova_igra</button>
    </form>

% elif poskus == model.PORAZ:

    <h1> IZGUBILI STE! </h1>

    <form action="/igra/" method="post">
        <button type="submit">Nova_igra</button>
    </form>

% else:

    <form action="/igra/" method="POST">
        Izbira: <input type="text" name="izbira">
        <button type="submit">Nova_igra</button>
    </form>

% end