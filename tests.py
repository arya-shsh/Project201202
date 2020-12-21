import unittest
from unittest.mock import patch
import project
import pygame
import shapes
from hashlib import sha256


class MockUserinput(unittest.TestCase):

    @patch('pygame.key.get_pressed')
    def test_exit_game(self, test_patch):
        """Патчим функцию pygame.key.get_pressed
        и заставляем его думать, что нажата стрелочка вправо

        Тест проверяет работает ли меню
        """
        test_patch.return_value = {pygame.K_RIGHT : True, pygame.K_LEFT : False}
        with self.assertRaises(SystemExit) as exit:
            project.main()
        self.assertEqual(exit.exception.code, 1)

    def test_compare_circle_to_premade(self):
        """Проверяет отрисовку круга"""
        screen = pygame.display.set_mode((100, 100))
        circle = shapes.Circle(50, 50, 100, (255,255,255), 0, 0)
        project.draw_smile(screen, circle, 100, 100, 100)
        pygame.image.save_extended(screen, ".circle_cache.png")
        sha = "095dbb844a99ec5b0d7d85b647cf041c84279221358eb1454042be4a8fb8433e"
        sha_circle = sha256()
        with open('.circle_cache.png', 'rb') as f:
            for byte_block in iter(lambda: f.read(4096),b""):
                sha_circle.update(byte_block)
        self.assertEqual(sha, sha_circle.hexdigest())

    def test_compare_square_to_premade(self):
        """Проверяет отрисовку квадрата"""
        screen = pygame.display.set_mode((100, 100))
        square = shapes.Rect(-1, -1, 101, 101, (255,255,255), 0, 0)
        project.draw_rect(screen, square)
        pygame.image.save_extended(screen, ".square_cache.png")
        sha = "525f896d2667232cb3b266a490c4e9fec2850dbf2d663d464d5e800d794fce82"
        sha_square = sha256()
        with open('.square_cache.png', 'rb') as f:
            for byte_block in iter(lambda: f.read(4096),b""):
                sha_square.update(byte_block)
        self.assertEqual(sha, sha_square.hexdigest())

    def test_color_out_of_range(self):
        """Проверяет отрисовку с некорректными цветами"""
        screen = pygame.display.set_mode((100, 100))
        square = shapes.Circle(-1, -1, 101, (255,255,255), 0, 0)
        self.assertRaises(ValueError, project.draw_smile, screen, square,
                          -100,-100,-100)


if __name__ == '__main__':
    unittest.main()

