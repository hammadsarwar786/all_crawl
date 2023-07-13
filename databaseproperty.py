import sqlite3

# Function to create a new database and table
def create_table():
    conn = sqlite3.connect('property.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS properties
    ( 
    id TEXT,
    area TEXT,
    bathroom_name TEXT,
    bathroom_value INTEGER,
    bedroom_name TEXT,
    bedroom_value INTEGER,
    category_id TEXT,
    category_identifier TEXT,
    completion_status TEXT,
    cts INTEGER,
    date_insert TEXT,
    default_price INTEGER,
    exclusive INTEGER,
    featured INTEGER,
    furnished TEXT,
    is_broker_project_property INTEGER,
    is_claimed_by_agent INTEGER,
    is_developer_property INTEGER,
    is_fair_price INTEGER,
    is_new_insert INTEGER,
    is_under_offer_by_competitor INTEGER,
    listing_level TEXT,
    listing_level_label TEXT,
    location_tree_path TEXT,
    name TEXT,
    new_projects INTEGER,
    offering_type TEXT,
    offering_type_id TEXT,
    premium INTEGER,
    price_on_application INTEGER,
    price_period_identifier TEXT,
    price_period_label TEXT,
    quality_score INTEGER,
    reference TEXT,
    rsp REAL,
    rss REAL,
    share_url TEXT,
    size INTEGER,
    size_unit TEXT,
    size_unit_identifier TEXT,
    smart_ad INTEGER,
    type_id TEXT,
    type_identifier TEXT,
    utilities_price_type TEXT,
    verified INTEGER,
    view_360 TEXT,
    image_broker TEXT,
    image_property TEXT,
    image_property_cts TEXT,
    image_property_floor_plan TEXT,
    image_property_homepage TEXT,
    image_property_medium TEXT,
    image_property_small TEXT,
    self_url TEXT,
    self_alternate_url TEXT
    )''')

    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_property(property_data):
    conn = sqlite3.connect('property.db')
    c = conn.cursor()

    # Extract attribute values from the property data
    id = property_data['id']
    area = property_data['attributes']['area']
    bathroom_name = property_data['attributes']['bathroom_name']
    bathroom_value = property_data['attributes']['bathroom_value']
    bedroom_name = property_data['attributes']['bedroom_name']
    bedroom_value = property_data['attributes']['bedroom_value']
    category_id = property_data['attributes']['category_id']
    category_identifier = property_data['attributes']['category_identifier']
    completion_status = property_data['attributes']['completion_status']
    cts = property_data['attributes']['cts']
    date_insert = property_data['attributes']['date_insert']
    default_price = property_data['attributes']['default_price']
    exclusive = property_data['attributes']['exclusive']
    featured = property_data['attributes']['featured']
    furnished = property_data['attributes']['furnished']
    is_broker_project_property = property_data['attributes']['is_broker_project_property']
    is_claimed_by_agent = property_data['attributes']['is_claimed_by_agent']
    is_developer_property = property_data['attributes']['is_developer_property']
    is_fair_price = property_data['attributes']['is_fair_price']
    is_new_insert = property_data['attributes']['is_new_insert']
    is_under_offer_by_competitor = property_data['attributes']['is_under_offer_by_competitor']
    listing_level = property_data['attributes']['listing_level']
    listing_level_label = property_data['attributes']['listing_level_label']
    location_tree_path = property_data['attributes']['location_tree_path']
    name = property_data['attributes']['name']
    new_projects = property_data['attributes']['new_projects']
    offering_type = property_data['attributes']['offering_type']
    offering_type_id = property_data['attributes']['offering_type_id']
    premium = property_data['attributes']['premium']
    price_on_application = property_data['attributes']['price_on_application']
    price_period_identifier = property_data['attributes']['price_period_identifier']
    price_period_label = property_data['attributes']['price_period_label']
    quality_score = property_data['attributes']['quality_score']
    reference = property_data['attributes']['reference']
    rsp = property_data['attributes']['rsp']
    rss = property_data['attributes']['rss']
    share_url = property_data['attributes']['share_url']
    size = property_data['attributes']['size']
    size_unit = property_data['attributes']['size_unit']
    size_unit_identifier = property_data['attributes']['size_unit_identifier']
    smart_ad = property_data['attributes']['smart_ad']
    type_id = property_data['attributes']['type_id']
    type_identifier = property_data['attributes']['type_identifier']
    utilities_price_type = property_data['attributes']['utilities_price_type']
    verified = property_data['attributes']['verified']
    view_360 = property_data['attributes']['view_360']
    image_broker = property_data['links']['image_broker']
    image_property = property_data['links']['image_property']
    image_property_cts = property_data['links']['image_property_cts']
    image_property_floor_plan = property_data['links']['image_property_floor_plan']
    image_property_homepage = property_data['links']['image_property_homepage']
    image_property_medium = property_data['links']['image_property_medium']
    image_property_small = property_data['links']['image_property_small']
    self_url = property_data['links']['self']
    self_alternate_url = property_data['links']['self_alternate']

    # Insert property data into the properties table
    c.execute('''INSERT INTO properties (id, area, bathroom_name, bathroom_value, bedroom_name, bedroom_value,
                     category_id, category_identifier, completion_status, cts, date_insert, default_price, exclusive,
                     featured, furnished, is_broker_project_property, is_claimed_by_agent, is_developer_property,
                     is_fair_price, is_new_insert, is_under_offer_by_competitor, listing_level, listing_level_label,
                     location_tree_path, name, new_projects, offering_type, offering_type_id, premium, price_on_application,
                     price_period_identifier, price_period_label, quality_score, reference, rsp, rss, share_url, size,
                     size_unit, size_unit_identifier, smart_ad, type_id, type_identifier, utilities_price_type, verified,
                     view_360,image_broker, image_property, image_property_cts, image_property_floor_plan,image_property_homepage,
                     image_property_medium, image_property_small, self_url, self_alternate_url)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (id, area, bathroom_name, bathroom_value, bedroom_name, bedroom_value, category_id, category_identifier,
               completion_status, cts, date_insert, default_price, exclusive, featured, furnished,
               is_broker_project_property, is_claimed_by_agent, is_developer_property, is_fair_price, is_new_insert,
               is_under_offer_by_competitor, listing_level, listing_level_label, location_tree_path, name, new_projects,
               offering_type, offering_type_id, premium, price_on_application, price_period_identifier,
               price_period_label, quality_score, reference, rsp, rss, share_url, size, size_unit,
               size_unit_identifier, smart_ad, type_id, type_identifier, utilities_price_type, verified, view_360,
               image_broker, image_property, image_property_cts, image_property_floor_plan,image_property_homepage, image_property_medium,
               image_property_small, self_url, self_alternate_url))

    conn.commit()
    conn.close()





