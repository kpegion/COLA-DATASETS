def src_header(title, open_catalog, url, tags, catalog_dir):
    ret =  src_header = """<!DOCTYPE html>
<html>
<head>
    <title>{0}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/bootswatch/3.3.7/cosmo/bootstrap.css">
    <link rel="stylesheet" href="static/pangeo-style.css">

</head>
<body>

<div id="navbar" class="navbar navbar-inverse navbar-default navbar-fixed-top">
    <div class="container">
        <div class="navbar-header">
            <!-- .btn-navbar is used as the toggle for collapsed navbar content -->
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".nav-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="/">
                <span><img src="img/cola.jpg"></span>
                COLA Catalog</a>
            <span class="navbar-text navbar-version pull-left"><b></b></span>
        </div>
        <div class="collapse navbar-collapse nav-collapse">
            <ul class="nav navbar-nav">
              <!--  <li><a href="https://medium.com/pangeo">Blog</a></li>
                <li><a href="https://discourse.pangeo.io">Forum</a></li> -->
            </ul>
        </div>
    </div>
</div>


<main role="main" class="container">
    <h1>{1}</h1>
    <div>
        <ol class="breadcrumb">

            <li><a href="master">master</a></li>

            <li><a href="TODO">TODO</a></li>

            <li class="active">{2}</li>

        </ol>
    </div>

    <div class="info">
         <!-- <h2></h2> -->

        <h3>Load in Python</h3>
        <pre><code class="language-python">from intake import open_catalog<br>
cat = open_catalog("{3}")
ds=cat.netcdf.read()</code></pre>

        <h3>Metadata</h3>
        <table class="table table-condensed table-hover">
            <tbody>

            <tr>
                <td>title</td>
                <td>{4}</td>
            </tr>

            <tr>
                <td>location</td>
                <td>{5}</td>
            </tr>

            <tr>
                <td>tags</td>
                <td>{6}</td>
            </tr>

            <tr>
                <td>catalog_dir</td>
                <td>{7}</td>
            </tr>

            </tbody>
        </table>
    </div>
    <div class="xarray">
        <h3>Dataset Contents</h3>

      <div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt output_prompt"></div>""".format(title, title, title, open_catalog, title, url, tags, catalog_dir)
    return ret




def src_footer():
    ret =    """</div>
  </div>

</main>


    
    <script src="//cdnjs.cloudflare.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="//cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
  </body>
</html>"""
    return ret