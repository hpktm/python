#!/usr/bin/env python


from bs4 import BeautifulSoup

html="""<!DOCTYPE HTML>
<html>
<head>
<title>White Edition</title>
<meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
<header>
  <nav class="main-nav">
    <ul>
      <li>
        <ul>
          <li><a href="index.html" class="active">about</a></li>
          <li><a href="projets.html">works</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </li>
    </ul>
  </nav>
</header>
<section id="video" class="home">
  <h1>WHITE EDITION</h1>
  <h2>E.S.T 2013</h2>
</section>
<section id="main-content" class="hitesh">
  <div class="text-intro">
    <h2>About</h2>
  </div>
  <div class="columns features">
    <div class="one-third first">
      <h3>Minimal</h3>
      <p>Bacon ipsum dolor sit amet cow ham beef, ground round t-bone meatloaf fatback sirloin pork chop swine pig. Venison shoulder prosciutto turkey tri-tip kielbasa andouille ham hock beef ribs. Meatloaf meatball doner filet mignon shankle.</p>
      <p><a href="#" class="more">En savoir plus</a></p>
    </div>
    <div class="one-third" data-pre="jony sanee">
      <h3>HTML5/CSS3</h3>
      <p>Chuck venison short ribs, pork loin strip steak turducken chicken boudin doner tail cow pork chop spare ribs.</p>
      <p><a href="#" class="more">En savoir plus</a></p>
    </div>
    <div class="one-third">
      <h3>Totally Free</h3>
      <p>Capicola prosciutto shankle frankfurter ham hock. Beef ribs t-bone rump, short ribs jerky turkey ham capicola pancetta filet mignon turducken boudin biltong venison shank.</p>
      <p><a href="#" class="more">En savoir plus</a></p>
    </div>
  </div>
</section>
<footer>
  <div class="copyright"><small>Copyright. All Rights Reserved | by <a target="_blank" rel="nofollow" href="http://www.iamsupview.be">Supview</a>.</small></div>
</footer>
</body>
</html>""";


soup=BeautifulSoup(html,'html.parser')


#direct

#print(soup.body)
#print(soup.head)
#print(soup.head.title)



#find()

#el=soup.find('div')



#find_all()

#el=soup.find_all('div')

# el=soup.find_all('div')[1]

#el=soup.find(id='video')

#el=soup.find(class_='hitesh')

#el=soup.find(attrs={"data-pre":"jony sanee"})




# select

#el=soup.select('#video')[0]

#el=soup.select('.hitesh')[0]



#get_text()

#el=soup.find(class_='hitesh').get_text()

# for item in soup.select(".one-third"):
#   print(item.get_text());



# Navigation

# el=soup.body.contents[1].contents[1].find_next_sibling()

# el=soup.find(id='video').find_previous_sibling()

el=soup.find(class_='one-third').find_parent()



print(el)