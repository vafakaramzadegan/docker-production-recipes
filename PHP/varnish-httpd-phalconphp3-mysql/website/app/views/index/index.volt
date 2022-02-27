<div class="jumbotron">
    <h1>Welcome to PhalconPHP 3.4</h1>
</div>

<div class="container">
    <div class="row">
        {% for post in posts %}
            <div class="col-sm">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ post.title }}</h5>
                        <p class="card-text">{{ post.body }}</p>
                        <a href="#" class="card-link">Continue Reading...</a>
                    </div>
                </div>
            </div>
        {% endfor %}
    </div>
</div>

<footer class="page-footer teal">
    <div class="footer-copyright text-center mt-5">
            Made with <span class="oi" data-glyph="heart"></span> by <a href="https://github.com/vafakaramzadegan">Vafa Karamzadegan</a>.
    </div>
</footer>