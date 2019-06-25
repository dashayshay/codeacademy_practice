class Art:
  def __init__(self,artist,title,medium,year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    return '{}. "{}". {}, {}, {}, {}.'.format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)
  
class Marketplace:
  def __init__(self):
    self.listings = []
    
  def __add__(self,new_listing):
    self.listings.append(new_listing)
    
  def remove_listing(self, listing):
    self.listings.remove(listing)
    
  def show_listings(self):
    for work in self.listings:
      print(work)
      
class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum
  
  
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
      
    
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller
  def __repr__(self):
    return '{} {}'.format(self.art.title, self.price)

veneer = Marketplace()
edytta = Client('Edytta Halprit', 'Private Collector', False)

moma = Client("The MOMA", "New York", True)
print(veneer.show_listings())

girl_with_mandolin = Art(artist ="Picasso, Pablo",title="Girl with a Mandolin (Fanny Tellier)",year=1910, medium="oil on canvas", owner =edytta)
print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin, '$6M(USD)')