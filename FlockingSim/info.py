def align(self, boids):
	steering = Vector(*np.zeros(2))
	total = 0
	avg_vec = Vector(*np.zeros(2))
	for boid in boids:
		if np.linalg.norm(boid.position - self.position) < self.perception:
			avg_vec += boid.velocity
			total += 1
	if total > 0:
		avg_vec /= total
		avg_vec = Vector(*avg_vec)
		avg_vec = (avg_vec /np.linalg.norm(avg_vec)) * self.max_speed
		steering = avg_vec - self.velocity

	return steering

def cohesion(self, boids):
	steering = Vector(*np.zeros(2))
	total = 0
	center_of_mass = Vector(*np.zeros(2))
	for boid in boids:
		if np.linalg.norm(boid.position - self.position) < self.perception:
			center_of_mass += boid.position
			total += 1
	if total > 0:
		center_of_mass /= total
		center_of_mass = Vector(*center_of_mass)
		vec_to_com = center_of_mass - self.position
		if np.linalg.norm(vec_to_com) > 0:
			vec_to_com = (vec_to_com / np.linalg.norm(vec_to_com)) * self.max_speed
		steering = vec_to_com - self.velocity
		if np.linalg.norm(steering)> self.max_force:
			steering = (steering /np.linalg.norm(steering)) * self.max_force

	return steering

def separation(self, boids):
	steering = Vector(*np.zeros(2))
	total = 0
	avg_vector = Vector(*np.zeros(2))
	for boid in boids:
		distance = np.linalg.norm(boid.position - self.position)
		if self.position != boid.position and distance < self.perception:
			diff = self.position - boid.position
			diff /= distance
			avg_vector += diff
			total += 1
	if total > 0:
		avg_vector /= total
		avg_vector = Vector(*avg_vector)
		if np.linalg.norm(steering) > 0:
			avg_vector = (avg_vector / np.linalg.norm(steering)) * self.max_speed
		steering = avg_vector - self.velocity
		if np.linalg.norm(steering)> self.max_force:
			steering = (steering /np.linalg.norm(steering)) * self.max_force

	return steering